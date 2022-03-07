from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' #serializer all the fields
        # or I can write one by one fields = ['id','name',]