# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.code'
        db.alter_column(u'warehouse_product', 'code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25))
        # Adding unique constraint on 'Product', fields ['code']
        db.create_unique(u'warehouse_product', ['code'])


    def backwards(self, orm):
        # Removing unique constraint on 'Product', fields ['code']
        db.delete_unique(u'warehouse_product', ['code'])


        # Changing field 'Product.code'
        db.alter_column(u'warehouse_product', 'code', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'warehouse.product': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Product'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
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