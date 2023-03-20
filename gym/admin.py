from django.contrib import admin

from gym.models import User

@admin.register(User)
class GymModelAdmin(admin.ModelAdmin):
    list_display=['id','email','sub_expired_on']