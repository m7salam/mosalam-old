from django.contrib import admin
from .models import Post, Category, Author

# Register your models here.
"""
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    pass
"""


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
