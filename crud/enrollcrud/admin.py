from django.contrib import admin
from .models import user
@admin.register(user)
class userform(admin.ModelAdmin):
    list_display=('id','name','email','password')
     
    
# Register your models here.
