from rest_framework.response import Response
from rest_framework.decorators import api_view
from baseapp.models import Item
from .serializers import ItemSerializers

@api_view(['GET'])
def getData(request):
    person={'name':'Aman','age':20}
    items=Item.objects.all()
    serializers=ItemSerializers(items,many=True)
    return Response(serializers.data)
    #return Response(person)

@api_view(['POST'])
def addItem(request):
    serializer=ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)