from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import curry
from portfolio.settings import PARSER
from utils import load_path_attr
import markdown

from datetime import datetime


class Company(models.Model):
    title= models.CharField(_("title"),max_length=100)
    slug=models.SlugField(max_length=50, unique=True)
    url = models.CharField(max_length=150, blank=True)
    location=models.CharField(_("Location"),max_length=100,blank=True)
    country=models.CharField(_('Country'),max_length=50,blank=True)
    
    def __unicode__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(_('title'),max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.skill_detail', (), {'slug': self.slug, })

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

    
class Project(models.Model):
    title = models.CharField(_('title'),max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    url = models.URLField(_('url'),blank=True, null=True)
    summary_txt = models.TextField(_('Summary'))
    summary_html = models.TextField(blank=True)
    description_txt = models.TextField(_('Description'))
    description_html = models.TextField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    company=models.ForeignKey(Company,blank=True,null=True)
    category = models.ForeignKey('Category',blank=True,null=True)
    skills = models.ManyToManyField('Skill', blank=True,null=True)
    
    class Meta:
        ordering = ['-start_date', '-end_date', ]

    def __unicode__(self):
        return self.title
        
    def save(self,**kwargs):
        render_func = curry(load_path_attr(PARSER[0], **PARSER[1]))
        
            
        self.summary_html = render_func(self.summary_txt)
        self.description_html = render_func(self.description_txt)
        
        super(Project, self).save(**kwargs)
        
    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.project_detail', (), {'slug': str(self.slug), })
        
class Image(models.Model):
    project = models.ForeignKey('Project',related_name="images")
    image_path = models.ImageField(upload_to="portfolio/image/%Y/%m/%d")
    title=models.CharField(blank=True,max_length=125)
    url = models.CharField(blank=True,max_length=255)

    def __unicode__(self):
        if self.pk is not None:
            return u"{{ %d }}" % (self.pk)
        else:
            return "deleted image"
        
class Video(models.Model):
    """
    Assumes that the videos are stored on hosting site such as youtube or vimeo
    """
    project = models.ForeignKey('Project',related_name='videos')
    title=models.CharField(_("title"),max_length=100)
    slug=models.SlugField(_('slug'),max_length=50,blank=True)
    caption=models.CharField(_('caption'),max_length=120,blank=True)
    url = models.CharField(blank=True,max_length=255)
    def __unicode__(self):
        if self.pk is not None:
            return u"{{ %d }} %s" % (self.pk,self.title)
        else:
            return "deleted video"
            
        
    
class File(models.Model):
    project = models.ForeignKey('Project',related_name='files')
    slug=models.SlugField(_('slug'),max_length=50,blank=True)
    caption=models.CharField(_('caption'),max_length=120,blank=True)
    file_path = models.FileField(upload_to="portfolio/file/%Y/%m/%d")
    timestamp = models.DateTimeField(default=datetime.now, editable=False)
    
    def __unicode__(self):
        if self.pk is not None:
            return u"{{ %d }} " % (self.pk)
        else:
            return "deleted file"

    def get_absolute_url(self):
        return self.file_path.url        


    
class Recommendation(models.Model):
    name=models.CharField(_("name"),max_length=125)
    position=models.CharField(_('position'),max_length=100,blank=True)
    project=models.ForeignKey(Project,related_name="recommendations",null=True,blank=True)
    slug = models.SlugField(_('slug'),max_length=50, unique=True)
    quotation_txt=models.TextField()
    quotation_html=models.TextField(blank=True)
    date=models.DateField(blank=True,null=True)
    
    def __unicode__(self):
        return u" ".join(self.quotation_txt.split()[:5])  



 
    
