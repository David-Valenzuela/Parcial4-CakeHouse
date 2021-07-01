from django.contrib import admin
from .models import Comuna, Pago, Producto
from .models import Ciudad
from .models import Cliente

admin.site.register(Cliente)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Producto)
admin.site.register(Pago)
