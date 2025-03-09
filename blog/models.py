from django.db import models
from django.shortcuts import reverse

class Post (models.Model):
    STAT_CHOICE = (
        ('pub' , 'publish'),
        ('drf', 'draft'),
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices= STAT_CHOICE, max_length = 5)

    def __str__(self):
        return self.title
    def get_absolute_url (self):
        return reverse('Posts_detail', args=[self.id])
