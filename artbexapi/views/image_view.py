from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import Image, Category


class ImageView(ViewSet):

    def retrieve(self, request, pk):
        image = Image.objects.get(pk=pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def list(self, request):

        images = []

        if "category" in request.query_params:
            image_category = request.query_params['category']
            images = Image.objects.filter(category=image_category)

        # images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArtBexCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for category
    """
    class Meta:
        model = Category
        fields = ('id', 'category')


class ImageSerializer(serializers.ModelSerializer):
    """JSON serializer for images
    """

    category = ArtBexCategorySerializer()

    class Meta:
        model = Image
        fields = ('id', 'type', 'imageUrl', 'category', )
