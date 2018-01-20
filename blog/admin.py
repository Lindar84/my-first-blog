from django.contrib import admin

# Register your models here.
from .models import Post    # == from blog.models import Post, tedy z aktualniho adresare

admin.site.register(Post)
