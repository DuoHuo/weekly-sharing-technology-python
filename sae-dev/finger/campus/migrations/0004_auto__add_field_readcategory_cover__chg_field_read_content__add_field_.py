# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ReadCategory.cover'
        db.add_column(u'campus_readcategory', 'cover',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Read.content'
        db.alter_column(u'campus_read', 'content', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))
        # Adding field 'ActivityCategory.cover'
        db.add_column(u'campus_activitycategory', 'cover',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SchoolInfoCategory.cover'
        db.add_column(u'campus_schoolinfocategory', 'cover',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SchoolInfo.date'
        db.add_column(u'campus_schoolinfo', 'date',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


        # Changing field 'SchoolInfo.content'
        db.alter_column(u'campus_schoolinfo', 'content', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Activity.content'
        db.alter_column(u'campus_activity', 'content', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Exam.content'
        db.alter_column(u'campus_exam', 'content', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))
        # Adding field 'ExamCategory.cover'
        db.add_column(u'campus_examcategory', 'cover',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ReadCategory.cover'
        db.delete_column(u'campus_readcategory', 'cover')


        # Changing field 'Read.content'
        db.alter_column(u'campus_read', 'content', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))
        # Deleting field 'ActivityCategory.cover'
        db.delete_column(u'campus_activitycategory', 'cover')

        # Deleting field 'SchoolInfoCategory.cover'
        db.delete_column(u'campus_schoolinfocategory', 'cover')

        # Deleting field 'SchoolInfo.date'
        db.delete_column(u'campus_schoolinfo', 'date')


        # Changing field 'SchoolInfo.content'
        db.alter_column(u'campus_schoolinfo', 'content', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Activity.content'
        db.alter_column(u'campus_activity', 'content', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Exam.content'
        db.alter_column(u'campus_exam', 'content', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))
        # Deleting field 'ExamCategory.cover'
        db.delete_column(u'campus_examcategory', 'cover')


    models = {
        u'campus.activity': {
            'Meta': {'object_name': 'Activity'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campus.ActivityCategory']", 'null': 'True', 'blank': 'True'})
        },
        u'campus.activitycategory': {
            'Meta': {'object_name': 'ActivityCategory'},
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'campus.exam': {
            'Meta': {'object_name': 'Exam'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campus.ExamCategory']", 'null': 'True', 'blank': 'True'})
        },
        u'campus.examcategory': {
            'Meta': {'object_name': 'ExamCategory'},
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'campus.read': {
            'Meta': {'object_name': 'Read'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campus.ReadCategory']", 'null': 'True', 'blank': 'True'})
        },
        u'campus.readcategory': {
            'Meta': {'object_name': 'ReadCategory'},
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'campus.schoolinfo': {
            'Meta': {'object_name': 'SchoolInfo'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['campus.SchoolInfoCategory']", 'null': 'True', 'blank': 'True'})
        },
        u'campus.schoolinfocategory': {
            'Meta': {'object_name': 'SchoolInfoCategory'},
            'cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['campus']