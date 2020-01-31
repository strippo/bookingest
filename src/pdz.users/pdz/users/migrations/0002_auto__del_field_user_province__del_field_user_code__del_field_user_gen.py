# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.province'
        db.delete_column(u'users_user', 'province')

        # Deleting field 'User.code'
        db.delete_column(u'users_user', 'code')

        # Deleting field 'User.gender'
        db.delete_column(u'users_user', 'gender')

        # Deleting field 'User.is_active'
        db.delete_column(u'users_user', 'is_active')

        # Deleting field 'User.possible_requests'
        db.delete_column(u'users_user', 'possible_requests')

        # Deleting field 'User.birth_date'
        db.delete_column(u'users_user', 'birth_date')

        # Deleting field 'User.tax_number'
        db.delete_column(u'users_user', 'tax_number')

        # Deleting field 'User.checkin_card'
        db.delete_column(u'users_user', 'checkin_card')

        # Adding field 'User.facebook_account'
        db.add_column(u'users_user', 'facebook_account',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'User.province'
        db.add_column(u'users_user', 'province',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.code'
        db.add_column(u'users_user', 'code',
                      self.gf('django.db.models.fields.CharField')(unique=True, max_length=15, null=True),
                      keep_default=False)

        # Adding field 'User.gender'
        db.add_column(u'users_user', 'gender',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'User.is_active'
        db.add_column(u'users_user', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'User.possible_requests'
        db.add_column(u'users_user', 'possible_requests',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.birth_date'
        db.add_column(u'users_user', 'birth_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.tax_number'
        db.add_column(u'users_user', 'tax_number',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16, blank=True),
                      keep_default=False)

        # Adding field 'User.checkin_card'
        db.add_column(u'users_user', 'checkin_card',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'User.facebook_account'
        db.delete_column(u'users_user', 'facebook_account')


    models = {
        u'users.user': {
            'Meta': {'ordering': "('surname', 'name')", 'object_name': 'User'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook_account': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
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