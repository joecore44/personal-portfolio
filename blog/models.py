from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/')
    content = models.TextField()
    category = models.CharField(max_length=24, null=True, blank=True,)
    type = models.CharField(max_length=100, null=True, blank=True,)
    client = models.CharField(max_length=100, null=True, blank=True,)
    project_link = models.CharField(max_length=100, null=True, blank=True)
    github_link = models.CharField(max_length=100, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class ResumeItem(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    tags = models.CharField(max_length=100, null=True, blank=True,)
    content = models.TextField()
    category = models.CharField(max_length=24, null=True, blank=True,)
    company_link = models.CharField(max_length=100)
    date_range = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    content = models.TextField()
    client = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Skill(models.Model):
    title = models.CharField(max_length=40)
    percentage = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title