from django.contrib import admin
from author.models import AuthorProfile,Category

# Register your models here.
admin.site.register(AuthorProfile)
admin.site.register(Category)
