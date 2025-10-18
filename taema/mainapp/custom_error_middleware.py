from django.shortcuts import render
from django.conf import settings



class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            if settings.DEBUG:
                # Replace default debug error with your own page
                return render(request, 'pages/500.html', status=500)
            raise
        if response.status_code == 404 and settings.DEBUG:
            return render(request, 'pages/404.html', status=404)
        return response
