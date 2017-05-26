from django.contrib import admin

# Register your models here.
from generic_views.models import Publisher,Book,Author
from basic.models import Task

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Task)