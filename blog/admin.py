from django.contrib import admin
from . models import Author, Blog

admin.site.register([Author,Blog])