from django.db import models
from django.contrib.auth.models import User

class WatchLaterEntry(models.Model):
    title = models.CharField(max_length=300)
    media_type = models.CharField(max_length=100)
    movie_id = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField("Date of Birth", blank=True, null=True)
    genre = models.CharField(max_length=300, default="")
    stream = models.CharField(max_length=300, default="")
    movies = models.CharField(max_length=1000, default="")
    watchlater = models.ManyToManyField(WatchLaterEntry)

    def __str__(self):
        return f'{self.user.username} Profile'

