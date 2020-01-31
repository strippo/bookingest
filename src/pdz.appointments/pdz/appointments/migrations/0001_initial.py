# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Appointment'
        db.create_table(u'appointments_appointment', (
            (u'event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['events.Event'], unique=True, primary_key=True)),
            ('operator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='appointments', to=orm['workers.Operator'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], blank=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['enum.Service'])),
        ))
        db.send_create_signal(u'appointments', ['Appointment'])


    def backwards(self, orm):
        # Deleting model 'Appointment'
        db.delete_table(u'appointments_appointment')


    models = {
        u'appointments.appointment': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Appointment', '_ormbases': [u'events.Event']},
            u'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['events.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'operator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'appointments'", 'to': "orm['workers.Operator']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enum.Service']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'blank': 'True'})
        },
        u'enum.service': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Service'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
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
        u'users.user': {
            'Meta': {'ordering': "('surname', 'name')", 'object_name': 'User'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'checkin_card': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'gender': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'possible_requests': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'tax_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
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

    complete_apps = ['appointments']