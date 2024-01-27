
import requests
from django.shortcuts import render
from django.views.decorators.http import require_GET
from webapp.models import UserIP




# Create your views here.
@require_GET
def get_public_ip(request):
    try:
        # Make a request to ipinfo.io to get the user's public IP
        response = requests.get('https://ipinfo.io')
        data = response.json()

        # Extract the public IP address from the response
        user_ip = data.get('ip', 'Unknown')

        # Check if the user's public IP is already in the database
        user_ip_obj, created = UserIP.objects.get_or_create(public_ip=user_ip)

        if created:
            # The user's public IP was not in the database, and it has been added
            message = 'User IP added to the database.'
        else:
            # The user's public IP was already in the database
            message = 'User IP already exists in the database.'
    except Exception as e:
        user_ip = 'Unknown'
        message = f'Error: {str(e)}'

    return render(request, 'webapp/index.html', context={'public_ip': user_ip})

def public_ips(request):
    userip = UserIP.objects.all()
    return render(request, 'webapp/table.html', context={'ips': userip})