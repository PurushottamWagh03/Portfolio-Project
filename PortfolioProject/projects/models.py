from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField()
    tech_stack = models.CharField(max_length=300)

    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)

    created_date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
