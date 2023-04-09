from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import Audience


class AudienceView(ViewSet):

    def retrieve(self, request, pk):
        audience = Audience.objects.get(pk=pk)
        serializer = AudienceSerializer(audience)
        return Response(serializer.data)


    def list(self, request):
        audiences = Audience.objects.all()
        serializer = AudienceSerializer(audiences, many=True)
        return Response(serializer.data)
    
class AudienceSerializer(serializers.ModelSerializer):
    """JSON serializer for audience
    """
    class Meta:
        model = Audience
        fields = ('id', 'type', )
