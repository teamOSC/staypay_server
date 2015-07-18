# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Appliances'
        db.create_table(u'hotel_appliances', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('appliance_id', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('on', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal(u'hotel', ['Appliances'])

        # Adding model 'Room'
        db.create_table(u'hotel_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hotel_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('user', self.gf('django.db.models.fields.CharField')(default=0, max_length=200)),
            ('room_server', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('room_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('type_id', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('appliances', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hotel.Appliances'], null=True)),
        ))
        db.send_create_signal(u'hotel', ['Room'])


    def backwards(self, orm):
        # Deleting model 'Appliances'
        db.delete_table(u'hotel_appliances')

        # Deleting model 'Room'
        db.delete_table(u'hotel_room')


    models = {
        u'hotel.appliances': {
            'Meta': {'object_name': 'Appliances'},
            'appliance_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'on': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'room_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        },
        u'hotel.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'hotel_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rooms': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hotel.HotelRooms']", 'null': 'True'})
        },
        u'hotel.hotelrooms': {
            'Meta': {'object_name': 'HotelRooms'},
            'available': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'beds': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'related_hotel_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'total': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'hotel.room': {
            'Meta': {'object_name': 'Room'},
            'appliances': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hotel.Appliances']", 'null': 'True'}),
            'hotel_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'room_server': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'type_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '200'})
        }
    }

    complete_apps = ['hotel']