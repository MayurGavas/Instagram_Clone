from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class NetworkEdge(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    class Meta:
        unique_together = ['from_user', 'to_user']
