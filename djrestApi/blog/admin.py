from django.contrib import admin

# Register your models here.
from .models import User

admin.site.register(User)
admin.site.site_header='Administración'
admin.site.site_title='Panel de administración'
admin.site.index_title='Bienvenido al Panel'
