from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from datetime import datetime


class Company(models.Model):
    title= models.CharField(_("title"),max_length=100)
    slug=models.SlugField(max_length=50, unique=True)
    url = models.CharField(max_length=150, blank=True)
    location=models.CharField(_("location"),max_length=100,blank=True)
    country=models.CharField(_('country'),max_length=50,blank=True)
    
    def __unicode__(self):
        return self.name


    
class Project(models.Model):
    title = models.CharField(_('title'),max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    url = models.URLField(_('url'),blank=True, null=True)
    short_description = models.TextField(_('summary'))
    description = models.TextField(_('description'))
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    company=models.ForeignKey(Company,blank=True,null=True)
    category = models.ForeignKey('Category',blank=True,null=True)
    features = models.ManyToManyField('Feature', blank=True,null=True)
    
    class Meta:
        ordering = ['-start_date', '-end_date', ]

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.project_detail', (), {'slug': str(self.slug), })
        
class ProjectImage(models.Model):
    project = models.ForeignKey('Project',related_name="project_images")
    image_path = models.ImageField(upload_to="project_image/%Y/%m/%d")
    slug = models.SlugField(_('slug'),max_length=50,blank=True)
    caption=models.CharField(max_length=120,blank=True)
    timestamp = models.DateTimeField(default=datetime.now, editable=False)
    url = models.CharField(blank=True,max_length=150)
    
   

    def __unicode__(self):
        if self.pk is not None:
            return u"{{ %d }} %s" % (self.pk)
        else:
            return "deleted image"
            
class ProjectFile(models.Model):
    project = models.ForeignKey('Project',related_name='files')
    slug=models.SlugField(_('slug'),max_length=50,blank=True)
    caption=models.CharField(_('caption'),max_length=120,blank=True)
    file_path = models.FileField(upload_to="project_file/%Y/%m/%d")
    timestamp = models.DateTimeField(default=datetime.now, editable=False)

    def __unicode__(self):
        if self.pk is not None:
             return u"{{ %d }} %s" % (self.pk,self.title)
        else:
            return "deleted file"

    def get_absolute_url(self):
        return self.file.url        

class Feature(models.Model):
    title = models.CharField(_('title'),max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.feature_detail', (), {'slug': self.slug, })

class Category(models.Model):
    title = models.CharField(_('title'),max_length=200)
    slug = models.SlugField(_('slug'),max_length=50, unique=True)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ["position"]

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.category_detail', (), {'slug': str(self.slug), })

    
class Reccomendation(models.Model):
    first_name=models.CharField(_("first_name"),max_length=60)
    last_name=models.CharField(_("last_name"),max_length=60)
    position=models.CharField(_('position'),max_length=100)
    projects=models.ForeignKey(Project,related_name="recommendations")
    slug = models.SlugField(_('slug'),max_length=50, unique=True)
    quotation=models.TextField()
    date=models.DateField(blank=True,null=True)
    def __unicode__(self):
        return u" ".join(self.quotation.split()[:5])  



 
    
