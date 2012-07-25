from django.contrib import admin
from portfolio.models import Project,Company,Skill,Category,File,Image,\
     Recommendation,Video

class ReccomendationInline(admin.TabularInline):
    model=Recommendation

class ImageInline(admin.TabularInline):
    model=Image
class FileInline(admin.TabularInline):
    model=File
    
class VideoInline(admin.TabularInline):
    model=Video    
  
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
    inlines = [
           ReccomendationInline,
           ImageInline,
           VideoInline,
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
admin.site.register(File)
admin.site.register(Image)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Recommendation)

