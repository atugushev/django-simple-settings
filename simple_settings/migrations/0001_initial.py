# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Settings'
        db.create_table(u'simple_settings_settings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('value_type', self.gf('django.db.models.fields.CharField')(default='str', max_length=10, blank=True)),
        ))
        db.send_create_signal(u'simple_settings', ['Settings'])


    def backwards(self, orm):
        # Deleting model 'Settings'
        db.delete_table(u'simple_settings_settings')


    models = {
        u'simple_settings.settings': {
            'Meta': {'object_name': 'Settings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'value_type': ('django.db.models.fields.CharField', [], {'default': "'str'", 'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['simple_settings']