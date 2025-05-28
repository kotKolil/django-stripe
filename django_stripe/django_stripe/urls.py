from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path('buy/<int:id>', create_checkout_session),
    path('item/<int:Id>', item_preview)
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
