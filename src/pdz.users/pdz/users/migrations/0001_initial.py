# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'users_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('tax_number', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15, unique=True, null=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gender', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('possible_requests', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('checkin_card', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['User'])

        # Adding model 'UserAttachment'
        db.create_table(u'users_userattachment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_files', to=orm['users.User'])),
            ('attachment', self.gf('protected_filefield.fields.ProtectedFileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['UserAttachment'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'users_user')

        # Deleting model 'UserAttachment'
        db.delete_table(u'users_userattachment')


    models = {
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
        u'users.userattachment': {
            'Meta': {'object_name': 'UserAttachment'},
            'attachment': ('protected_filefield.fields.ProtectedFileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_files'", 'to': u"orm['users.User']"})
        }
    }

    complete_apps = ['users']