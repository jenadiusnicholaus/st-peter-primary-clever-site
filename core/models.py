from django.conf import settings
from django.db import models
from django.utils import timezone


class blog(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='blog', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Blog Post'

    def __str__(self):
        return str(self.author)


class comment(models.Model):
    content = models.TextField(null=True)
    create_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Comment'

    def __str__(self):
        return str(self.post)


class Contact(models.Model):
    user_name = models.CharField(max_length=200, null=True, blank=200)
    user_email = models.CharField(max_length=200, null=True, blank=200)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Messages from unregistered users'

    def __str__(self):
        return str(self.user_name)

