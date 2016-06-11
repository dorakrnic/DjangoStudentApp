from django.contrib import admin
from .models import Student, Predmet, Ocena
# Register your models here.

#admin.site.register(Student)
admin.site.register(Predmet)
#admin.site.register(Ocena)

class StoreAdminStudent(admin.ModelAdmin):
      list_display = ('studentIme','studentPrezime','index')
      list_editable = ('studentIme','studentPrezime')

admin.site.register(Student, StoreAdminStudent)

class StoreAdminOcena(admin.ModelAdmin):
      list_display = ('student','predmet','ocena')
      
admin.site.register(Ocena, StoreAdminOcena)

