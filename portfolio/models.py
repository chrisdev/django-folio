from django.db import models
from imagekit.models import ImageModel
from django_countries import CountryField
from django.utils.translation import ugettext_lazy as _, ugettext
from taggit.managers import TaggableManager

class Company(models.Model):
    name= models.CharField(_("name"),max_length=100)
    slug=models.SlugField(max_length=50, unique=True)
    address_line1= models.CharField(_("address"), max_length=75,)
    address_line2= models.CharField(_("       "),max_length=75, blank=True)
   
    city = models.CharField(_("city or town"),max_length=75)
    state= models.CharField(_("state/province.."),max_length=75,blank=True)
    postal_code=models.CharField(_("zip or postal code"),max_length=30,blank=True)
    country=CountryField()
    home_phone = models.CharField(_("home phone"),max_length=100,blank=True)
    mobile_phone= models.CharField(_("mobile phone"),max_length=100,blank=True)
    office_phone= models.CharField(_("office phone"),max_length=100,blank=True)
    
    def __unicode__(self):
        return self.name

    
class Person(models.Model):
    first_name=models.CharField(_("first_name"),max_length=60)
    last_name=models.CharField(_("last_name"),max_length=60)
    position=models.CharField(_('position'),max_length=100)
    company=models.ForeignKey(Company,blank=True)
    def __unicode__(self):
        return u"%s %s" % (self.first_name,self.last_name)
    
class Quote(models.Model):
    person=models.ForeignKey(Person)
    slug = models.SlugField(max_length=50, unique=True)
    quotation=models.TextField()
    date=models.DateField(blank=True)
    def __unicode__(self):
        return u" ".join(self.quotation.split()[:5])

    
class Project(models.Model):
    name = models.CharField(_('name'),max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    url = models.URLField(_('url'),blank=True, null=True)
    short_description = models.TextField(_('summary'))
    description = models.TextField(_('description'))
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey('Category',blank=True,null=True)
    skills = models.ManyToManyField('Skill', blank=True,null=True)
    client=models.ForeignKey(Company)
    tags=TaggableManager()
    
    class Meta:
        ordering = ['-start_date', '-end_date', ]

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.project_detail', (), {'slug': str(self.slug), })

class Skill(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.skill_detail', (), {'slug': str(self.slug), })

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ["position"]

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.category_detail', (), {'slug': str(self.slug), })

class ProjectFile(models.Model):
    project = models.ForeignKey('Project')
    file = models.FileField(upload_to="project_file/%Y/%m/%d")
    desc = models.TextField()

    def __unicode__(self):
        return self.file.name

    def get_absolute_url(self):
        return self.file.url

class ProjectImage(ImageModel):
    project = models.ForeignKey('Project')
    image = models.ImageField(upload_to="project_image/%Y/%m/%d")
    desc = models.TextField()
    num_views=models.PositiveIntegerField(editable=False,default=0)

    def __unicode__(self):
        return self.image.name

    def get_absolute_url(self):
        return self.image.url
    
    class IKOptions:
        # This inner class is where we define the ImageKit options for the model
        spec_module = 'portfolio.specs'
        cache_dir = 'project/%Y/%m/%d'
        image_field = 'image'
        save_count_as = 'num_views'

 
    
