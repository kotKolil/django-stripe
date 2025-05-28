function buy (id, api_token) {

    const stripe = Stripe(api_token)

    // Call your backend to create the Checkout Session
    fetch(`/buy/${id}`, {
    method: 'GET',
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(session) {
        return stripe.redirectToCheckout({ sessionId: session.id });
    })
    .then(function(result) {
        if (result.error) {
            alert(result.error.message);
            }
        });

}