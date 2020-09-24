from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

CATS = [
    ('Digital', 'Digital'),
    ('StartUp', 'StartUp')
]


class Tag(models.Model):
    tag_name = models.CharField(max_length=40)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    category = models.CharField(choices=CATS, max_length=200)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
