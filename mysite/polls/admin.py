
# Register your models here.
from django.contrib import admin
from polls.models import MyModel
from polls.company import Company
# Register your models here.

admin.site.register(MyModel)
admin.site.register(Company)
# admin.site.register(NewModel)
