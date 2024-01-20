from collections.abc import Iterable
from django.urls import reverse
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=False)
    thumbnail = models.ImageField(
        upload_to="products/tb/%Y/%m/%d", blank=False, editable=False
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_thumbnail()

    def create_thumbnail(self):
        if self.image:
            img = Image.open(self.image.path)
            thumbnail_size = (200, 200)
            img.thumbnail(thumbnail_size)
            thumbnail_io = BytesIO()
            filename, extension = os.path.splitext(os.path.basename(self.image.name))
            img.save(
                thumbnail_io, format="JPEG" if extension.lower() == "jpg" else "PNG"
            )
            thumbnail_name = f"thumbnail_{filename}{extension.lower()}"
            thumbnail_file = SimpleUploadedFile(thumbnail_name, thumbnail_io.getvalue())
            self.thumbnail.save(thumbnail_file.name, thumbnail_file, save=False)
            super().save()
