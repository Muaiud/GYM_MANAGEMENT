from django.contrib import admin

from gym.models import User,Contact

@admin.register(User)
class GymModelAdmin(admin.ModelAdmin):
    list_display=['id','email','sub_expired_on']
@admin.register(Contact) 
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','contact','message']        