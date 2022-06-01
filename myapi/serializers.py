from rest_framework import serializers
from .models import prenatal

class PrenatalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = prenatal
        fields = ('id', 'name', 'mae', 'cns', 'unidade')
