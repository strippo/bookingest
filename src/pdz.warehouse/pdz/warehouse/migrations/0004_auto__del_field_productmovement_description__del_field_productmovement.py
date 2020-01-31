# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ProductMovement.description'
        db.delete_column(u'warehouse_productmovement', 'description')

        # Deleting field 'ProductMovement.title'
        db.delete_column(u'warehouse_productmovement', 'title')


    def backwards(self, orm):
        # Adding field 'ProductMovement.description'
        db.add_column(u'warehouse_productmovement', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'ProductMovement.title'
        db.add_column(u'warehouse_productmovement', 'title',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)


    models = {
        u'warehouse.product': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Product'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'warehouse.productmovement': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'ProductMovement'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'movement_type': ('django.db.models.fields.IntegerField', [], {}),
            'operator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_movements'", 'to': "orm['workers.Operator']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'movements'", 'to': u"orm['warehouse.Product']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'workers.operator': {
            'Meta': {'ordering': "('surname', 'name')", 'object_name': 'Operator'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        }
    }

    complete_apps = ['warehouse']