from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import Tone


class ToneView(ViewSet):

    def retrieve(self, request, pk):
        tone = Tone.objects.get(pk=pk)
        serializer = ToneSerializer(tone)
        return Response(serializer.data)


    def list(self, request):
        tones = Tone.objects.all()
        serializer = ToneSerializer(tones, many=True)
        return Response(serializer.data)
    
class ToneSerializer(serializers.ModelSerializer):
    """JSON serializer for tone
    """
    class Meta:
        model = Tone
        fields = ('id', 'type', )
