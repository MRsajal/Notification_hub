"""
Paste this into your   config/urls.py
(replace or merge with what you already have)
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ── your existing routes stay here ──
    path('api/', include('api.urls')),          # keep whatever you had

    # ── add this for the notification dashboard ──
    path('notifications/', include('notifications.urls')),
]

# Visit: http://127.0.0.1:8000/notifications/
#
# Want it at the root ( http://127.0.0.1:8000/ ) instead?
# Change the line above to:
#   path('', include('notifications.urls')),
# Make sure it is the LAST entry in urlpatterns.
