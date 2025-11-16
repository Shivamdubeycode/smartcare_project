# create_superuser.py
from django.contrib.auth.models import User

username = "shivam"
email = "shivamdub22ey@gmail.com"
password = "Shiv1234@106"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)