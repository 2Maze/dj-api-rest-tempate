from api.v1 import views
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('health', csrf_exempt(views.BaseApiView.as_view({'get': 'health'}))),
    # path('balance', csrf_exempt(views.BaseApiView.as_view({'get': 'balance'}))),
]
