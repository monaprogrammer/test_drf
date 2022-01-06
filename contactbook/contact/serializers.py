from rest_framework import serializers
from .models import ContactDetail


class ShowContactDetailSerializer(serializers.ModelSerializer):

       class Meta:
           model = ContactDetail
           fields = '__all__'

class AddContactDetailSerializer(serializers.ModelSerializer):

       class Meta:
           model = ContactDetail
           fields = '__all__'