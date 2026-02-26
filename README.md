# Notification Hub – Django Project

A company-wide notification dashboard built with Django.  
Currently uses **static data** — replacing with a real API requires editing one function in `notifications/data.py`.

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run development server
python manage.py runserver

# 3. Open browser
http://127.0.0.1:8000/
```

---

## Project Structure

```
notification_hub/
├── manage.py
├── requirements.txt
├── notification_hub/       # Django project config
│   ├── settings.py
│   └── urls.py
└── notifications/          # Main app
    ├── data.py             ← SWAP STATIC DATA WITH API HERE
    ├── views.py
    ├── urls.py
    ├── templatetags/
    │   └── notification_extras.py
    └── templates/
        └── notifications/
            └── dashboard.html
```

---

## Connecting a Real API

Open `notifications/data.py` and replace the body of `get_all_notifications()`:

```python
def get_all_notifications() -> dict:
    import requests
    response = requests.get(
        'https://your-api.example.com/notifications/',
        headers={'Authorization': 'Bearer YOUR_TOKEN'}
    )
    return response.json()   # must match the expected schema
```

Expected JSON schema per notification type:
```json
{
  "EHS Notification": {
    "columns": ["Code", "Details", ...],
    "data": [{"Code": "EHS-001", "Details": "...", ...}],
    "count": 3
  },
  ...
}
```

---

## Endpoints

| URL | Description |
|-----|-------------|
| `/` | Main dashboard |
| `/?type=EHS+Notification` | Filter to a specific type |
| `/api/notifications/` | JSON – all notifications |
| `/api/notifications/?type=EHS+Notification` | JSON – single type |
