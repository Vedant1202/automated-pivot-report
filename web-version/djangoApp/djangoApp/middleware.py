from django.shortcuts import redirect
from django.urls import reverse

class RedirectUnauthenticatedMiddleware:
    """Middleware to redirect unauthenticated users to the login page."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Check if the request is not for the login page
            if request.path != reverse('login'):
                return redirect('login')  # Redirect to the login page
        
        response = self.get_response(request)
        return response
