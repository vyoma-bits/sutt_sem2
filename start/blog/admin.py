from django.contrib import admin
from .models import train,Trip_info,person,trip3,events,locations,plans,expense,CustomUser

admin.site.register(train)
admin.site.register(Trip_info)
admin.site.register(person)
admin.site.register(trip3)
admin.site.register(events)
admin.site.register(locations)
admin.site.register(plans)
admin.site.register(CustomUser)
admin.site.register(expense)

# Register your models here.
