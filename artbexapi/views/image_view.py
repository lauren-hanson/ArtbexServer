from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import Image


class ImageView(ViewSet):

    def retrieve(self, request, pk):
        image = Image.objects.get(pk=pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def list(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)


class ImageSerializer(serializers.ModelSerializer):
    """JSON serializer for image
    """
    class Meta:
        model = Image
        fields = ('id', 'type', 'imageUrl', )
