from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Item
import stripe

from .config import *


def create_checkout_session(request, Id):
    try:
        item = get_object_or_404(Item, pk=Id)

        stripe.api_key = API_KEY

        payment_intent = stripe.PaymentIntent.create(
          amount=item.price,
          currency="usd",
          automatic_payment_methods={"enabled": True},
        )




        return JsonResponse(
            data={
                "data": payment_intent["client_secret"]
            }
        )
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def item_preview(request, Id):
    item = get_object_or_404(Item, pk=Id)

    return render(
        request,
        template_name="item_preview.html",
        context={
            "item": item.name,
            "description": item.description,
            "price": item.price,
            "id": item.id,
            "secret_key": API_KEY,
            "publish_key": PUBLISH_KEY
        }
    )


def index(request):
    return HttpResponse("<h3>It works!</h3>")
