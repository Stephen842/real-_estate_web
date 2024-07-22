from django.utils.timezone import now
from .models import UserVisit
import requests

class UserVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        #To get the IP address of users
        ip_address = request.META.get('REMOTE_ADDR')

        #To get user's location
        location_data = self.get_location(ip_address)

        #create a new visit record
        UserVisit.objects.create(
            visited_at=now(),
            ip_address = ip_address,
            location=location_data
        )
        return response

    def get_location(self, ip_address):
        response  = requests.get(f'https://ipinfo.io/{ip_address}/json')
        return response.json() if response.status_code == 200 else {}
