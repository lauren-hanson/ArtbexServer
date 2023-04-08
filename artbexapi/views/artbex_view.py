from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import ArtBex


class ArtBexView(ViewSet):

    def retrieve(self, request, pk):
        artbex = ArtBex.objects.get(pk=pk)
        serializer = ArtBexSerializer(artbex)
        return Response(serializer.data)


    def list(self, request):
        artbexs = ArtBex.objects.all()
        serializer = ArtBexSerializer(artbexs, many=True)
        return Response(serializer.data)
    
class ArtBexSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = ArtBex
        fields = ('id', 'tone', 'startDate', 'endDate', 'creator', 'notes', )
