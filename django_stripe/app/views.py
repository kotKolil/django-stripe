from django.http import *
from django.shortcuts import render

from .models import Item
import stripe

from .config import *


def create_checkout_session(request, id):
    item = Item.objects.get(Id=id)

    stripe.api_key = API_KEY

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000',
        cancel_url='http://127.0.0.1:8000',
    )

    return JsonResponse(
        data = {
            "id": session['id']
        }
    )

def item_preview(request, Id):
    item = Item.objects.get(Id=Id)

    return render(request,
                  template_name = "item_preview.html",
                  context = {
                    "item":item.name,
                    "description":item.description,
                    "price": item.price,
                    "id": item.Id,
                    "secret_key": API_KEY,
                    "publish_key": PUBLISH_KEY
                  }
              )

def index(request):
    return HttpResponse("<h3>It works!</h3>")