from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import Format


class FormatView(ViewSet):

    def retrieve(self, request, pk):
        format = Format.objects.get(pk=pk)
        serializer = FormatSerializer(format)
        return Response(serializer.data)


    def list(self, request):
        formats = Format.objects.all()
        serializer = FormatSerializer(formats, many=True)
        return Response(serializer.data)
    
class FormatSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Format
        fields = ('id', 'type', )
