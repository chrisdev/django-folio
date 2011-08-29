from django.contrib import admin
from portfolio.models import *
class PersonInline(admin.TabularInline):
    model=Person
    
class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("name",)}
    inlines = [
           PersonInline,
        ]
    
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(ProjectFile)
admin.site.register(ProjectImage)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Quote)


