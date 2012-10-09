from django.contrib import admin

from blog.posts import models

admin.site.register(models.Post)
