from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def snippet_list(request,format=None):
    if request.method=='GET':
        snippets=Snippet.objects.all()
        serializer=SnippetsSerializer(snippets,many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=SnippetsSerializer(data=request.data)
        # data=JSONParser().parse(request)
        # serializer=SnippetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        #     return JsonResponse(serializer.data,status=201)
        # return JsonResponse(serializer.errors,status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetsSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = SnippetsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
