from django.contrib import admin
from service.models import Service
class serviceadmin(admin.ModelAdmin):
    list_display=('service_title', 'service_des')


admin.site.register(Service,serviceadmin)
# Register your models here.
