from django.contrib import admin
from .models import KospiData, Kosdaq, Report, Capitalzation, Kospicap

# Register your models here.
admin.site.register(KospiData)
admin.site.register(Kosdaq)
admin.site.register(Report)
admin.site.register(Capitalzation)
admin.site.register(Kospicap)