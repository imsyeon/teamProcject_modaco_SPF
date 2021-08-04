from django.contrib import admin
<<<<<<< Updated upstream
from .models import KospiData, Kosdaq, Report, Capitalzation, Kospicap
=======
from .models import KospiData, Kosdaq, Report
>>>>>>> Stashed changes

# Register your models here.
admin.site.register(KospiData)
admin.site.register(Kosdaq)
<<<<<<< Updated upstream
admin.site.register(Report)
admin.site.register(Capitalzation)
admin.site.register(Kospicap)
=======
admin.site.register(Report)
>>>>>>> Stashed changes
