from django.contrib import admin
from portfolio.models import Project,Company,Feature,Category,ProjectFile,ProjectImage,\
     Recommendation,ProjectVideo

class ReccomendationInline(admin.TabularInline):
    model=Recommendation

class ImageInline(admin.TabularInline):
    model=ProjectImage
class FileInline(admin.TabularInline):
    model=ProjectFile
class VideoInline(admin.TabularInline):
    model=ProjectVideo    

  
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

class FeatureAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}    
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
          
admin.site.register(Project,ProjectAdmin)
admin.site.register(Feature,FeatureAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(ProjectFile)
admin.site.register(ProjectImage)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Recommendation)


