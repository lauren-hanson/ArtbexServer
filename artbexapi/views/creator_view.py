from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import Creator


class CreatorView(ViewSet):

    def retrieve(self, request, pk):
        creator = Creator.objects.get(pk=pk)
        serializer = CreatorSerializer(creator)
        return Response(serializer.data)


    def list(self, request):
        creators = Creator.objects.all()
        serializer = CreatorSerializer(creators, many=True)
        return Response(serializer.data)
    
class CreatorSerializer(serializers.ModelSerializer):
    """JSON serializer for creator
    """
    class Meta:
        model = Creator
        fields = ('id', 'firstName', 'lastName', 'email',  )
