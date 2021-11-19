from django.contrib import admin
from .models import Pr
from .models import Client
from .models import Rack
from .models import Room

class PrAdmin(admin.ModelAdmin):
    list_display = ('height', 'width', 'length', 'weight', 'recdate', 'nofcon', 'client', 'content', 'expdate', 'rack', 'numofpos')
    list_display_links = ('nofcon',)
    search_fields = ('recdate', 'nofcon', 'content', 'expdate')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'requisites')
    list_display_links = ('name',)
    search_fields = ('name', 'requisites')

class RackAdmin(admin.ModelAdmin):
    list_display = ('number', 'room', 'seats', 'H', 'W', 'L', 'load')
    list_display_links = ('number',)
    search_fields = ('number',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('namer', 'V')
    list_display_links = ('namer',)
    search_fields = ('namer',)

admin.site.register(Pr, PrAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Rack, RackAdmin)
admin.site.register(Room, RoomAdmin)