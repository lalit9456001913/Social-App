from django.contrib import admin
from twitter.models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(Liked)
admin.site.register(Dislike)