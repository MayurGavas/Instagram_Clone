from django.db import models
from django.contrib.auth.models import User


class Timestamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(Timestamp):
    location = models.CharField(max_length=50, blank=True)
    caption_heading = models.CharField(max_length=50, blank=False)
    caption_text = models.CharField(max_length=500, blank=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_by')
    is_published = models.BooleanField(default=False)


class MediaHandeling(Timestamp):

    seq_no = models.PositiveSmallIntegerField(default=0)
    media_file = models.FileField(upload_to='Posts/')
    media_under_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_media')

    class Meta:
        unique_together = ['seq_no', 'media_file']





