from rest_framework import serializers

from applications.models import I90Application


class I90ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = I90Application
        fields = '__all__'
