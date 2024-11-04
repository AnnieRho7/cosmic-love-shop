// Ensure you replace 'YOUR_PUBLIC_STRIPE_KEY' with your actual Stripe public key.
const stripe = Stripe('YOUR_PUBLIC_STRIPE_KEY'); // Replace with your actual Stripe public key

// Get the checkout button
const checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', function () {
    // Make a request to your server to create a checkout session
    fetch('/cart/checkout/', {  // Update this line to match the URL in your urls.py
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Fetch CSRF token
        },
        body: JSON.stringify({
            // Include any necessary data for the session if needed
        }),
    })
    .then(function (response) {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(function (sessionId) {
        return stripe.redirectToCheckout({ sessionId: sessionId.id }); // Ensure the correct property for sessionId
    })
    .then(function (result) {
        if (result.error) {
            alert(result.error.message);
        }
    })
    .catch(function (error) {
        console.error('Error:', error);
    });
});

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
