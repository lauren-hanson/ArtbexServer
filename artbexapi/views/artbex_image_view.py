from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import ArtBexImage, ArtBex, Image


class ArtBexImageView(ViewSet):

    def retrieve(self, request, pk):
        artBexImage = ArtBexImage.objects.get(pk=pk)
        serializer = ArtBexImageSerializer(artBexImage)
        return Response(serializer.data)

    def list(self, request):
        artBexImages = ArtBexImage.objects.all()
        serializer = ArtBexImageSerializer(artBexImages, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations to create an ArtBexImage

        Returns
            Response -- JSON serialized ArtBexImage
        """
        try:
            artbex = ArtBex.objects.get(pk=request.data['artbex_id'])
            image = Image.objects.get(pk=request.data['image_id'])
        except (ArtBex.DoesNotExist, Image.DoesNotExist):
            return Response({'message': 'You sent an invalid artbex or image PK'}, status=status.HTTP_404_NOT_FOUND)

        artbeximage = ArtBexImage.objects.create(
            artbex=artbex,
            image=image
        )

        serializer = ArtBexImageSerializer(artbeximage)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ArtBexImageSerializer(serializers.ModelSerializer):
    """JSON serializer for artBexImage
    """
    class Meta:
        model = ArtBexImage
        fields = ('artbex', 'image',)
