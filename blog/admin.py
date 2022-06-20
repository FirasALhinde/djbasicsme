from django.contrib import admin

# Register your models here.

from.models import Post,Category

class PostAdmin(admin.ModelAdmin):
    list_display = ["id","title","category"]
    search_fields = ["title","content"]
    date_hierarchy = "publish_date"

admin.site.register(Post,PostAdmin)
admin.site.register(Category)