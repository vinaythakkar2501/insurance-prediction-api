from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from mlpredict.models import LifeData, MedicalData,features,CarData

class FeaturesSerializers(serializers.ModelSerializer):

    class Meta:
        model = features
        fields = ('__all__')

class MedicalDataSerializaers(serializers.ModelSerializer):
    class Meta:
        model = MedicalData
        fields = ('__all__')


class LifeDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = LifeData
        fields = ('__all__')

class CarDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarData
        fields = ('__all__')