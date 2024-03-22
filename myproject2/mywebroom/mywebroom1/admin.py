from django.contrib import admin
from .models import user, Booking, Person, Room

# Register your models here.
admin.site.register(user)
admin.site.register(Person)
admin.site.register(Room)
admin.site.register(Booking)
