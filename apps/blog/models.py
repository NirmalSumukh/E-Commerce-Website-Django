from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field  
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    DRAFT, PUBLISHED = "draft", "published"
    STATUS_CHOICES = [(DRAFT, "Draft"), (PUBLISHED, "Published")]

    title       = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=200, unique=True, blank=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                    null=True, blank=True, related_name="posts")
    excerpt     = models.TextField(max_length=300, blank=True)
    content = CKEditor5Field(config_name="blog", null=True)
    featured    = models.ImageField(upload_to="blog/featured/", blank=True, null=True)
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    tags        = TaggableManager(blank=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.status == self.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
