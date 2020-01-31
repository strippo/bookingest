# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.price'
        db.add_column(u'warehouse_product', 'price',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.price'
        db.delete_column(u'warehouse_product', 'price')


    models = {
        u'warehouse.product': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Product'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'warehouse.productmovement': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'ProductMovement'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'movement_type': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True'}),
            'operator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'product_movements'", 'null': 'True', 'to': "orm['workers.Operator']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'movements'", 'to': u"orm['warehouse.Product']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'workers.operator': {
            'Meta': {'ordering': "('surname', 'name')", 'object_name': 'Operator'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        }
    }

    complete_apps = ['warehouse']