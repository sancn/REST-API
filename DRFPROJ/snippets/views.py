from snippets.models import Snippet
from snippets.serializers import SnippetsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):
    def get(self, request, format=None):
        snippet=Snippet.objects.all()
        serializer=SnippetsSerializer(snippet,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=SnippetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
class SnippetDetail(APIView):
    def get_object(self,pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        snippet=Snippet.objects.all()
        serializer=SnippetsSerializer(snippet)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        snippet=self.get_object(pk)
        seralizer=SnippetsSerializer(snippet,data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data,status=status.HTTP_200_OK)
        return Response(seralizer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format='json'):
        snippet=self.get_object(pk)
        del snippet
        return Response(status=status.HTTP_204_NO_CONTENT)