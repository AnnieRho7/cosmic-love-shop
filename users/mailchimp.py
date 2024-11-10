from django.conf import settings
import mailchimp_marketing


class MailchimpService:
    def __init__(self):
        self.client = mailchimp_marketing.Client()
        self.client.set_config({
            "api_key": settings.MAILCHIMP_API_KEY,
            "server": settings.MAILCHIMP_REGION
        })
