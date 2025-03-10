from django.apps import AppConfig
import threading
from .views import start_background_task  # Import the function

class DjangoWebAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoWebApp'

    def ready(self):
        """Start the background task when Django starts."""
        print("[INFO] Starting automatic IGNITE data fetching task...")
        threading.Thread(target=start_background_task, daemon=True).start()
