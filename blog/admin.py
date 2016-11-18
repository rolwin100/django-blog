from django.contrib import admin
from blog.models import Post
from blog.models import Bloglist
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display=['title','description']
	list_filter=['published','created']
	search_fields=['description','title','content']
	date_hierarchy='created'
	save_on_top=True
	prepopulated_fields={"slug":("title",)}

class BlogAdmin(admin.ModelAdmin):
	list_display=['title1','description1']
	list_filter=['published1','created1']
	search_fields=['description1','title1','content1']
	date_hierarchy='created1'
	save_on_top=True

admin.site.register(Post,PostAdmin)
admin.site.register(Bloglist,BlogAdmin)