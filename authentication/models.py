from django.db import models
from django.contrib.auth.models import AbstractUser
from review.models import UserFollows


class User(AbstractUser):
    pass
