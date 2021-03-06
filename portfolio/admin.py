from django.contrib import admin
from portfolio.models import Project,Company,Skill,Category,File,Image,\
     Recommendation,Video
try:
  from markitup.widgets import AdminMarkItUpWidget as content_widget
except ImportError:
   content_widget=forms.Textarea
   
class ReccomendationInline(admin.StackedInline):
    model=Recommendation
    exclude=('quotation_html',)
class ImageInline(admin.TabularInline):
    model=Image
class FileInline(admin.TabularInline):
    model=File
    
class VideoInline(admin.TabularInline):
    model=Video    
    
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
    exclude=('summary_html','description_html')
    inlines = [
           ReccomendationInline,
           ImageInline,
           VideoInline,
           FileInline, 
        ]
    def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name in ('summary_txt','description_txt'):
			kwargs['widget'] = content_widget()
		return super(ProjectAdmin, self).formfield_for_dbfield(db_field, **kwargs)
		
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

