# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ProjectFile'
        db.delete_table('portfolio_projectfile')

        # Deleting model 'ProjectVideo'
        db.delete_table('portfolio_projectvideo')

        # Deleting model 'ProjectImage'
        db.delete_table('portfolio_projectimage')

        # Deleting model 'Feature'
        db.delete_table('portfolio_feature')

        # Adding model 'Image'
        db.create_table('portfolio_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['portfolio.Project'])),
            ('image_path', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('portfolio', ['Image'])

        # Adding model 'Video'
        db.create_table('portfolio_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videos', to=orm['portfolio.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('portfolio', ['Video'])

        # Adding model 'Skill'
        db.create_table('portfolio_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('portfolio', ['Skill'])

        # Adding model 'File'
        db.create_table('portfolio_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['portfolio.Project'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('file_path', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('portfolio', ['File'])

        # Deleting field 'Project.description'
        db.delete_column('portfolio_project', 'description')

        # Deleting field 'Project.short_description'
        db.delete_column('portfolio_project', 'short_description')

        # Adding field 'Project.summary_txt'
        db.add_column('portfolio_project', 'summary_txt', self.gf('django.db.models.fields.TextField')(default='funky'), keep_default=False)

        # Adding field 'Project.summary_html'
        db.add_column('portfolio_project', 'summary_html', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Project.description_txt'
        db.add_column('portfolio_project', 'description_txt', self.gf('django.db.models.fields.TextField')(default='test'), keep_default=False)

        # Adding field 'Project.description_html'
        db.add_column('portfolio_project', 'description_html', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Removing M2M table for field features on 'Project'
        db.delete_table('portfolio_project_features')

        # Adding M2M table for field skills on 'Project'
        db.create_table('portfolio_project_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['portfolio.project'], null=False)),
            ('skill', models.ForeignKey(orm['portfolio.skill'], null=False))
        ))
        db.create_unique('portfolio_project_skills', ['project_id', 'skill_id'])

        # Deleting field 'Recommendation.last_name'
        db.delete_column('portfolio_recommendation', 'last_name')

        # Deleting field 'Recommendation.first_name'
        db.delete_column('portfolio_recommendation', 'first_name')

        # Deleting field 'Recommendation.projects'
        db.delete_column('portfolio_recommendation', 'projects_id')

        # Deleting field 'Recommendation.quotation'
        db.delete_column('portfolio_recommendation', 'quotation')

        # Adding field 'Recommendation.name'
        db.add_column('portfolio_recommendation', 'name', self.gf('django.db.models.fields.CharField')(default=2, max_length=125), keep_default=False)

        # Adding field 'Recommendation.project'
        db.add_column('portfolio_recommendation', 'project', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='recommendations', null=True, to=orm['portfolio.Project']), keep_default=False)

        # Adding field 'Recommendation.quotation_txt'
        db.add_column('portfolio_recommendation', 'quotation_txt', self.gf('django.db.models.fields.TextField')(default='test'), keep_default=False)

        # Adding field 'Recommendation.quotation_html'
        db.add_column('portfolio_recommendation', 'quotation_html', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'ProjectFile'
        db.create_table('portfolio_projectfile', (
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('file_path', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['portfolio.Project'])),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(blank=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('portfolio', ['ProjectFile'])

        # Adding model 'ProjectVideo'
        db.create_table('portfolio_projectvideo', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(blank=True, max_length=50, db_index=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videos', to=orm['portfolio.Project'])),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('portfolio', ['ProjectVideo'])

        # Adding model 'ProjectImage'
        db.create_table('portfolio_projectimage', (
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['portfolio.Project'])),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('image_path', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(blank=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('portfolio', ['ProjectImage'])

        # Adding model 'Feature'
        db.create_table('portfolio_feature', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
        ))
        db.send_create_signal('portfolio', ['Feature'])

        # Deleting model 'Image'
        db.delete_table('portfolio_image')

        # Deleting model 'Video'
        db.delete_table('portfolio_video')

        # Deleting model 'Skill'
        db.delete_table('portfolio_skill')

        # Deleting model 'File'
        db.delete_table('portfolio_file')

        # Adding field 'Project.description'
        db.add_column('portfolio_project', 'description', self.gf('django.db.models.fields.TextField')(default='funky'), keep_default=False)

        # Adding field 'Project.short_description'
        db.add_column('portfolio_project', 'short_description', self.gf('django.db.models.fields.TextField')(default='funky'), keep_default=False)

        # Deleting field 'Project.summary_txt'
        db.delete_column('portfolio_project', 'summary_txt')

        # Deleting field 'Project.summary_html'
        db.delete_column('portfolio_project', 'summary_html')

        # Deleting field 'Project.description_txt'
        db.delete_column('portfolio_project', 'description_txt')

        # Deleting field 'Project.description_html'
        db.delete_column('portfolio_project', 'description_html')

        # Adding M2M table for field features on 'Project'
        db.create_table('portfolio_project_features', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['portfolio.project'], null=False)),
            ('feature', models.ForeignKey(orm['portfolio.feature'], null=False))
        ))
        db.create_unique('portfolio_project_features', ['project_id', 'feature_id'])

        # Removing M2M table for field skills on 'Project'
        db.delete_table('portfolio_project_skills')

        # Adding field 'Recommendation.last_name'
        db.add_column('portfolio_recommendation', 'last_name', self.gf('django.db.models.fields.CharField')(default='boo', max_length=60), keep_default=False)

        # Adding field 'Recommendation.first_name'
        db.add_column('portfolio_recommendation', 'first_name', self.gf('django.db.models.fields.CharField')(default='bush', max_length=60), keep_default=False)

        # Adding field 'Recommendation.projects'
        db.add_column('portfolio_recommendation', 'projects', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='recommendations', to=orm['portfolio.Project']), keep_default=False)

        # Adding field 'Recommendation.quotation'
        db.add_column('portfolio_recommendation', 'quotation', self.gf('django.db.models.fields.TextField')(default=1), keep_default=False)

        # Deleting field 'Recommendation.name'
        db.delete_column('portfolio_recommendation', 'name')

        # Deleting field 'Recommendation.project'
        db.delete_column('portfolio_recommendation', 'project_id')

        # Deleting field 'Recommendation.quotation_txt'
        db.delete_column('portfolio_recommendation', 'quotation_txt')

        # Deleting field 'Recommendation.quotation_html'
        db.delete_column('portfolio_recommendation', 'quotation_html')


    models = {
        'portfolio.category': {
            'Meta': {'ordering': "['position']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.company': {
            'Meta': {'object_name': 'Company'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        'portfolio.file': {
            'Meta': {'object_name': 'File'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'file_path': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': "orm['portfolio.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'portfolio.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['portfolio.Project']"}),
            'title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'portfolio.project': {
            'Meta': {'ordering': "['-start_date', '-end_date']", 'object_name': 'Project'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Category']", 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Company']", 'null': 'True', 'blank': 'True'}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_txt': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['portfolio.Skill']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'summary_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'summary_txt': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'portfolio.recommendation': {
            'Meta': {'object_name': 'Recommendation'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'recommendations'", 'null': 'True', 'to': "orm['portfolio.Project']"}),
            'quotation_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'quotation_txt': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'portfolio.skill': {
            'Meta': {'ordering': "['title']", 'object_name': 'Skill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.video': {
            'Meta': {'object_name': 'Video'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['portfolio.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']
