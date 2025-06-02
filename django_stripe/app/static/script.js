const stripe = Stripe("")
const elements = stripe.elements();
const cardElement = elements.create('card');

window.onload = () =>
{
    cardElement.mount('#card-element');
}

function buy (id,) {

    // Call your backend to create the Checkout Session
    fetch(`/buy/${id}`, {
    method: 'GET',
    })
    .then(function(response) {
        return response.json();
    })

.then(data => {
         stripe.confirmCardPayment(`${data.data}`, {
            payment_method: {
                card: cardElement,
                billing_details: {
                    name: 'John Doe',
                },
            },
        })
 .then( (data) => {
        console.log(data)
        if (data.error) {
            alert(`error: ${data.error.message}`)
            return
        }
        window.location.replace ("/")
     }
    )
    }
  );

}