// Get the values passed from Django using json_script
var stripe_public_key = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
var client_secret = JSON.parse(document.getElementById('id_client_secret').textContent);

// Initialize Stripe with the public key
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

// Define styling for the card input element
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create and mount the Stripe card input element
var card = elements.create('card', {style: style});
card.mount('#card-element');
