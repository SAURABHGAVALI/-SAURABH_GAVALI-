from django.contrib import admin
from blog.models import Post
from blog.models import Yoga
from blog.models import GYM
from blog.models import MEDITATION
from blog.models import ADVENTURE
from blog.models import Post
from blog.models import PRANIC


class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','created','publish')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)

class YogaAdmin(admin.ModelAdmin):
    list_display=['Cname','age','Email','MobileNo','Gender']

admin.site.register(Yoga,YogaAdmin)


class GYMAdmin(admin.ModelAdmin):
    list_display=['TraineeName','age','Email','MobileNo','Gender','City_Name']

admin.site.register(GYM,GYMAdmin)


class MEDITATIONAdmin(admin.ModelAdmin):
    list_display=['Name','age','Email','MobileNo','Gender','City_Name']

admin.site.register(MEDITATION,MEDITATIONAdmin)


class ADVENTUREAdmin(admin.ModelAdmin):
    list_display=['Name','age','Email','MobileNo','Gender','City_Name']

admin.site.register(ADVENTURE,ADVENTUREAdmin)


class PRANICAdmin(admin.ModelAdmin):
    list_display=['Name','age','Email','MobileNo','Gender','City_Name']

admin.site.register(PRANIC,PRANICAdmin)
