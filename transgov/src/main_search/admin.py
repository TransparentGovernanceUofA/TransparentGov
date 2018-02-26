from django.contrib import admin

from .models import Meeting, Category


admin.site.register(Category)



class MeetingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Meeting, MeetingAdmin)
