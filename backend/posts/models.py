from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail' kwargs={'pk': self.id})
