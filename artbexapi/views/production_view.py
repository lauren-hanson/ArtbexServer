from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from artbexapi.models import Production


class ProductionView(ViewSet):

    def retrieve(self, request, pk):
        production = Production.objects.get(pk=pk)
        serializer = ProductionSerializer(production)
        return Response(serializer.data)


    def list(self, request):
        productions = Production.objects.all()
        serializer = ProductionSerializer(productions, many=True)
        return Response(serializer.data)
    
class ProductionSerializer(serializers.ModelSerializer):
    """JSON serializer for production
    """
    class Meta:
        model = Production
        fields = ('id', 'type', 'imageUrl', )
