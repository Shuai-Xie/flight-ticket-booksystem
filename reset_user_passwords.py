"""

http://www.zzhgod.com/blog/3/post/django-admin-83
python manage.py shell

在 Python 终端执行以下命令
"""
from django.contrib.auth.models import User

user = User.objects.get(username='admin')
user.set_password('admin123')
user.save()