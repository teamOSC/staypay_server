# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HotelRooms'
        db.create_table(u'hotel_hotelrooms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('total', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('available', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('rate', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('beds', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'hotel', ['HotelRooms'])

        # Adding model 'Hotel'
        db.create_table(u'hotel_hotel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hotel_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('logo', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'hotel', ['Hotel'])


    def backwards(self, orm):
        # Deleting model 'HotelRooms'
        db.delete_table(u'hotel_hotelrooms')

        # Deleting model 'Hotel'
        db.delete_table(u'hotel_hotel')


    models = {
        u'hotel.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'hotel_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'hotel.hotelrooms': {
            'Meta': {'object_name': 'HotelRooms'},
            'available': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'beds': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'total': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hotel']