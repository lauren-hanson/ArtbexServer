from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import ArtBexImage


class ArtBexImageView(ViewSet):

    def retrieve(self, request, pk):
        artBexImage = ArtBexImage.objects.get(pk=pk)
        serializer = ArtBexImageSerializer(artBexImage)
        return Response(serializer.data)

    def list(self, request):
        artBexImages = ArtBexImage.objects.all()
        serializer = ArtBexImageSerializer(artBexImages, many=True)
        return Response(serializer.data)


class ArtBexImageSerializer(serializers.ModelSerializer):
    """JSON serializer for artBexImage
    """
    class Meta:
        model = ArtBexImage
        fields = ('artbex', 'image',  )
