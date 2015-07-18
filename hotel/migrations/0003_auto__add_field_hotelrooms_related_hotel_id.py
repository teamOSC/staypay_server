# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HotelRooms.related_hotel_id'
        db.add_column(u'hotel_hotelrooms', 'related_hotel_id',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'HotelRooms.related_hotel_id'
        db.delete_column(u'hotel_hotelrooms', 'related_hotel_id')


    models = {
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
        }
    }

    complete_apps = ['hotel']