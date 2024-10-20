from django.db import models
from petstagram.photos.models import Photo


class Comment(models.Model):
    MAX_LENGTH_TEXT = 300

    text = models.TextField(max_length=MAX_LENGTH_TEXT)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)