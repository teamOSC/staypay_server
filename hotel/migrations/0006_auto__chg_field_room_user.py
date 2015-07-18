# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Room.user'
        db.alter_column(u'hotel_room', 'user', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Room.user'
        db.alter_column(u'hotel_room', 'user', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'hotel.appliances': {
            'Meta': {'object_name': 'Appliances'},
            'appliance_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'hotel_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
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
            'user': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['hotel']