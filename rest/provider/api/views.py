# from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from base.models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_class=[permissions.IsAuthenticated]
# inside the decorators , we put in the methods we want like POST, GET, DELETE, PUT
# @api_view(['GET'])
# def getData(request):
#     #person = {'name': 'Olivia', 'age': 40} dummy data
#     items = Item.objects.all()
#     serializer = ItemSerializer(items, many=True) #if only gonna serializer one item , set many =False 
#     return Response(serializer.data)
 
# @api_view(['POST'])
# def addItem(request):
#       serializer = ItemSerializer(data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#       return Response(serializer.data)    
  
   
# @api_view(['PUT'])
# def updateItem(request,pk):
#    #update data  
#     if  request.method == 'PUT':
#         serializer = ItemSerializer( data=request.data)
#         if serializer.is_valid():
#                 serializer.save()
#     return Response(serializer.data)   
  
