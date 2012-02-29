from django.contrib import admin
from portfolio.models import Project,Company,Skill,Category,ProjectFile,ProjectImage,Reccomendation

class ReccomendationInline(admin.TabularInline):
    model=Reccomendation

class ImageInline(admin.TabularInline):
    model=ProjectImage
class FileInline(admin.TabularInline):
    model=ProjectFile
       

  
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("name",)}
    inlines = [
           ImageInline,
           ReccomendationInline,
           FileInline,
           
        ]

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}

class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}    
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
          
admin.site.register(Project,ProjectAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(ProjectFile)
admin.site.register(ProjectImage)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Reccomendation)


