# UpTrader-task
Task from https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit?tab=t.0

## Setup

- Install python requrements with pip `pip install -r requrements.txt`
- Create db (sqlite3) and apply migrations `python manage.py migrate`
- Create superuser `python manage.py createsupersuer` follow with CLI hints
- Launch server `python manage.py runserver`
- Visit http://localhost:8000/admin to create menu items
- After create menu items visit http://localhost:8000/
