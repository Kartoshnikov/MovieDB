from django.contrib import admin

# Register your models here.
from .models import Person, Citizen


#admin.site.register(Citizen)
class PersonInline(admin.StackedInline):
	model = Person
	extra = 3


class CitizenAdmin(admin.ModelAdmin):
	fields = ['citizen']
	inlines = [PersonInline]	
	list_display = ('citizen',)


class PersonAdmin(admin.ModelAdmin):
	fieldsets = [
		('Main Infornation', { 'fields': ['name', 'age',] }),
		('Citizen',	     { 'fields': ['citizen'] }),
	]
	list_display = ('name', 'age', 'citizen', 'votes')


admin.site.register(Citizen, CitizenAdmin)
admin.site.register(Person, PersonAdmin)
