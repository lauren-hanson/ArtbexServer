from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import ArtBex, Image
# , Audience, Tone, Production, Format


class ArtBexView(ViewSet):

    def retrieve(self, request, pk):
        artbex = ArtBex.objects.get(pk=pk)
        serializer = ArtBexSerializer(artbex)
        return Response(serializer.data)

    def list(self, request):
        artbexs = ArtBex.objects.all()
        serializer = ArtBexSerializer(artbexs, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized artbex instance
        """
        # try:
        #     creator = Creator.objects.get(user=request.auth.user)
        # except Creator.DoesNotExist:
        #     return Response({'message': 'You sent an invalid token'}, status=status.HTTP_404_NOT_FOUND)

        # try:
        #     audience = Audience.objects.get(pk=request.data['audience'])
        # except Audience.DoesNotExist:
        #     return Response({'message': 'You sent an invalid audience Id'}, status=status.HTTP_404_NOT_FOUND)

        # try:
        #     format = Format.objects.get(pk=request.data['format'])
        # except Format.DoesNotExist:
        #     return Response({'message': 'You sent an invalid format Id'}, status=status.HTTP_404_NOT_FOUND)

        # try:
        #     tone = Tone.objects.get(pk=request.data['tone'])
        # except Tone.DoesNotExist:
        #     return Response({'message': 'You sent an invalid tone Id'}, status=status.HTTP_404_NOT_FOUND)

        # try:
        #     production = Production.objects.get(pk=request.data['production'])
        # except Production.DoesNotExist:
        #     return Response({'message': 'You sent an invalid production Id'}, status=status.HTTP_404_NOT_FOUND)

        try:
            image = Image.objects.get(pk=request.data['image'])
        except Image.DoesNotExist:
            return Response({'message': 'You sent an invalid image Id'}, status=status.HTTP_404_NOT_FOUND)

        artbex = ArtBex.objects.create(
            # creator=creator,
            # audience=audience,
            # tone=tone,
            # format=format,
            # production=production,
            image=image,
            startDate=request.data['startDate'],
            endDate=request.data['endDate'],
            notes=request.data['notes'],

        )

        serializer = ArtBexSerializer(artbex)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):

        # try:
        #     creator = Creator.objects.get(user=request.auth.user)
        # except Creator.DoesNotExist:
        #     return Response({'message': 'You sent an invalid token'}, status=status.HTTP_404_NOT_FOUND)

        # try:
        #     audience = Audience.objects.get(pk=request.data['audience'])
        # except Audience.DoesNotExist:
        #     return Response({'message': 'You sent an invalid audience Id'}, status=status.HTTP_404_NOT_FOUND)

        # try:
        #     format = Format.objects.get(pk=request.data['format'])
        # except Format.DoesNotExist:
        #     return Response({'message': 'You sent an invalid format Id'}, status=status.HTTP_404_NOT_FOUND)

        # try:
        #     tone = Tone.objects.get(pk=request.data['tone'])
        # except Tone.DoesNotExist:
        #     return Response({'message': 'You sent an invalid tone Id'}, status=status.HTTP_404_NOT_FOUND)

        # try:
        #     production = Production.objects.get(pk=request.data['production'])
        # except Production.DoesNotExist:
        #     return Response({'message': 'You sent an invalid production Id'}, status=status.HTTP_404_NOT_FOUND)

        try:
            image = Image.objects.get(pk=request.data['image'])
        except Image.DoesNotExist:
            return Response({'message': 'You sent an invalid image Id'}, status=status.HTTP_404_NOT_FOUND)

        artbex_to_update = ArtBex.objects.get(pk=pk)
        # artbex_to_update.audience = audience
        # artbex_to_update.tone = tone
        # artbex_to_update.format = format
        # artbex_to_update.production = production
        artbex_to_update.image = image
        artbex_to_update.startDate = request.data['startDate']
        artbex_to_update.endDate = request.data['endDate']
        artbex_to_update.notes = request.data['notes']

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        artbex = ArtBex.objects.get(pk=pk)
        artbex.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ArtBexSerializer(serializers.ModelSerializer):
    """JSON serializer for artbex creations
    """
    class Meta:
        model = ArtBex
        fields = ('id', 'image',
                  'startDate', 'endDate', 'notes', )
