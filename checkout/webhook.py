import stripe
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from users.models import Order
import logging

logger = logging.getLogger(__name__)

def stripe_webhook(request):
    """Listen for webhooks from Stripe."""
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        logger.error(f"Invalid payload: {e}")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.error(f"Invalid signature: {e}")
        return HttpResponse(status=400)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return HttpResponse(status=500)

    logger.info(f"Received event: {event['type']}")

    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        order_id = payment_intent.metadata.get('order_id')

        if not order_id:
            logger.error('No order_id found in payment_intent metadata')
            return HttpResponse(status=400)

        try:
            order = Order.objects.get(order_number=order_id)
            order.status = 'Paid'
            order.save()
            logger.info(f"Order {order_id} marked as paid")
        except Order.DoesNotExist:
            logger.error(f"Order {order_id} not found")
            return HttpResponse(status=404)


    elif event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        order_id = payment_intent.metadata.get('order_id')

        if not order_id:
            logger.error('No order_id found in payment_intent metadata for failed payment')
            return HttpResponse(status=400)

        try:
            order = Order.objects.get(order_number=order_id)
            order.status = 'Payment Failed'
            order.save()
            logger.info(f"Order {order_id} marked as payment failed")
        except Order.DoesNotExist:
            logger.error(f"Order {order_id} not found")
            return HttpResponse(status=404)

    else:
        logger.info(f"Unhandled event type: {event['type']}")

    return JsonResponse({'status': 'success'})
