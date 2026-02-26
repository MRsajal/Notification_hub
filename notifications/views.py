from django.shortcuts import render
from django.http import JsonResponse
from .data import get_all_notifications, get_notification_by_type


def dashboard(request):
    """Main notification dashboard view."""
    all_notifications = get_all_notifications()
    active_type = request.GET.get('type', list(all_notifications.keys())[0])
    active_data = all_notifications.get(active_type, {})

    context = {
        "notification_types": list(all_notifications.keys()),
        "notification_counts": {k: v["count"] for k, v in all_notifications.items()},
        "active_type": active_type,
        "active_columns": active_data.get("columns", []),
        "active_rows": active_data.get("data", []),
        "active_count": active_data.get("count", 0),
        "total_notifications": sum(v["count"] for v in all_notifications.values()),
    }
    return render(request, "notifications/dashboard.html", context)


def api_notifications(request):
    """JSON API endpoint – swap static data for real API calls in data.py."""
    notification_type = request.GET.get('type')
    if notification_type:
        data = get_notification_by_type(notification_type)
        if data is None:
            return JsonResponse({"error": "Notification type not found"}, status=404)
        return JsonResponse({"type": notification_type, **data})
    return JsonResponse({"notifications": get_all_notifications()})
