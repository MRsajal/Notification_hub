# HOW TO INTEGRATE notifications app into your existing Django project
# =====================================================================
# Your project uses config.urls — just add 2 things:

# ── STEP 1: Add to your config/urls.py ──────────────────────────────
#
#   from django.contrib import admin
#   from django.urls import path, include
#
#   urlpatterns = [
#       path('admin/', admin.site.urls),
#       path('api/', ...),                          # your existing routes
#       path('notifications/', include('notifications.urls')),  # ← ADD THIS
#   ]
#
#   Then visit: http://127.0.0.1:8000/notifications/
#
#   ── OR to serve at root (http://127.0.0.1:8000/) ──
#
#   urlpatterns = [
#       path('admin/', admin.site.urls),
#       path('api/', ...),
#       path('', include('notifications.urls')),    # ← ADD THIS (must be last)
#   ]

# ── STEP 2: Add to your INSTALLED_APPS in settings.py ───────────────
#
#   INSTALLED_APPS = [
#       ...
#       'notifications',    # ← ADD THIS
#   ]

# That's it! Copy the entire `notifications/` folder into your project root.
