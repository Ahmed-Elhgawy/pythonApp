from django.urls import path
from webapp.views import get_public_ip, public_ips

urlpatterns = [
    path('', get_public_ip),
    path('all_ips', public_ips, name='all')
]