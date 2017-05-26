from django.contrib import admin

# Register your models here.
from practise2.models import MyModel
from datetime import datetime

class MymodelAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"time":(str(datetime.now()),)}
    class Meta:
       list_display = ["name","age"]

admin.site.register(MyModel,MymodelAdmin)