from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    subtitle = models.CharField(
        max_length=255, blank=True)  # Make subtitle optional
    content = models.TextField()  # Use TextField for longer blog content
    published_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('draft', 'Draft'),
        ('published', 'Published')
    ])

    def __str__(self) -> str:
        return self.title
