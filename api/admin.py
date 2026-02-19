from django.contrib import admin
from .models import *

admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Veiculo)
admin.site.register(Medicao)
admin.site.register(UnidadeMedida)
admin.site.register(MedicaoVeiculo)