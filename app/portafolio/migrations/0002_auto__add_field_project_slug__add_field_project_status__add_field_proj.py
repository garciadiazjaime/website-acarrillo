# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.slug'
        db.add_column(u'portafolio_project', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=140),
                      keep_default=False)

        # Adding field 'Project.status'
        db.add_column(u'portafolio_project', 'status',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Project.weight'
        db.add_column(u'portafolio_project', 'weight',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.weight'
        db.add_column(u'portafolio_item', 'weight',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.slug'
        db.delete_column(u'portafolio_project', 'slug')

        # Deleting field 'Project.status'
        db.delete_column(u'portafolio_project', 'status')

        # Deleting field 'Project.weight'
        db.delete_column(u'portafolio_project', 'weight')

        # Deleting field 'Item.weight'
        db.delete_column(u'portafolio_item', 'weight')


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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentor': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['portafolio']