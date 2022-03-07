from rest_framework import serializers

from main.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    resource_identifier = serializers.CharField(source='identifier.value')

    class Meta:
        model = Resource
        fields = ['id', 'resource_identifier', 'name', 'short_name', 'description', 'version', 'valid_from']


# class RecordSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Record
#         # fields = ['url', 'username', 'email', 'groups']