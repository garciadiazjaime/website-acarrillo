# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.mentor'
        db.delete_column(u'portafolio_project', 'mentor')


        # Changing field 'Project.description'
        db.alter_column(u'portafolio_project', 'description', self.gf('django.db.models.fields.TextField')(max_length=500))

        # Changing field 'Item.image'
        db.alter_column(u'portafolio_item', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):
        # Adding field 'Project.mentor'
        db.add_column(u'portafolio_project', 'mentor',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=140),
                      keep_default=False)


        # Changing field 'Project.description'
        db.alter_column(u'portafolio_project', 'description', self.gf('django.db.models.fields.CharField')(max_length=140))

        # Changing field 'Item.image'
        db.alter_column(u'portafolio_item', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

    models = {
        u'portafolio.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['portafolio.Project']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'portafolio.project': {
            'Meta': {'object_name': 'Project'},
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['portafolio']