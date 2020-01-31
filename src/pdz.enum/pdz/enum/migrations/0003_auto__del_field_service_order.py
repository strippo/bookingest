# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Service.order'
        db.delete_column(u'enum_service', 'order')


    def backwards(self, orm):
        # Adding field 'Service.order'
        db.add_column(u'enum_service', 'order',
                      self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True),
                      keep_default=False)


    models = {
        u'enum.service': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Service'},
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['enum']