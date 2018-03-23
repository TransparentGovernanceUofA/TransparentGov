from django.contrib import admin

from .models import Meeting, Subsection, Items, Motions, Presenters

admin.site.register(Motions)
admin.site.register(Presenters)
admin.site.register(Items)
admin.site.register(Subsection)
admin.site.register(Meeting)
