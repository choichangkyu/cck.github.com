# coding: utf-8
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=200)
    text = models.TextField()
    password = models.CharField(max_length=100, default="1111")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="1111")
    post = models.ForeignKey('wPlayGame.Post', related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
