from django.shortcuts import render

# Create your views here.
from . models import mymodel
from .serializers import mymodelserializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination




class PaginationView(APIView):
   
    def get(self, request, format=None):
      
        page_size = request.GET.get('page_size')
        
        if page_size is not None and page_size.isdigit():
            page_size = int(page_size)
        else:
           
            page_size = 2

        paginator = PageNumberPagination()
        paginator.page_size = page_size 

        queryset = mymodel.objects.all()
        context = paginator.paginate_queryset(queryset, request)
        serializer = mymodelserializers(context, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = mymodelserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk, format=None):
        queryset =mymodel.objects.filter(id=pk).first()
        serializer = mymodelserializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset= mymodel.objects.filter(id=pk).first()
        queryset.delete()
        return Response({"succes:deleted"})
