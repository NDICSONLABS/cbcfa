release: python manage.py migrate
release: python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
web: gunicorn cbcfa.wsgi