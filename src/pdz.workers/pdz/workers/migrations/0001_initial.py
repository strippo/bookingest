# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Operator'
        db.create_table(u'workers_operator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=35)),
        ))
        db.send_create_signal('workers', ['Operator'])

        # Adding model 'OperatorAvailability'
        db.create_table(u'workers_operatoravailability', (
            (u'event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['events.Event'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'workers', ['OperatorAvailability'])


    def backwards(self, orm):
        # Deleting model 'Operator'
        db.delete_table(u'workers_operator')

        # Deleting model 'OperatorAvailability'
        db.delete_table(u'workers_operatoravailability')


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'workers.operator': {
            'Meta': {'ordering': "('surname', 'name')", 'object_name': 'Operator'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        u'workers.operatoravailability': {
            'Meta': {'object_name': 'OperatorAvailability', '_ormbases': [u'events.Event']},
            u'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['events.Event']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['workers']