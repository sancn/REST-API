from snippets.models import Snippet
from snippets.serializers import SnippetsSerializers
from snippets.serializers import UserSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import renderers,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
# from rest_framework.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import BasePermission
from snippets.premissions import IsOwnerOrReadOnly
from rest_framework import status

# from rest_framework.permissions import BasePermission




# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset=Snippet.objects.all()
#     serializer_class=SnippetsSerializers

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#  create_user   def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
    
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
    
#     queryset=Snippet.objects.all()
#     serializer_class=SnippetsSerializers
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

# class SnippetList(generics.ListCreateAPIView):
#     queryset=Snippet.objects.all()
#     serializer_class=SnippetsSerializers


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Snippet.objects.all()
#     serializer_class=SnippetsSerializers

#################################
#################################
###################################
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def create_user(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


"""Replacing Snippetlist,SnippetDetail,SnippetHighlight
           with single class SnippetViewset"""
class SnippetViewSet(viewsets.ModelViewSet):
        queryset=Snippet.objects.all()
        serializer_class=SnippetsSerializers
        permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly] 

        @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
        def highlight(self, request, *args, **kwargs):
            snippet = self.get_object()
            return Response(snippet.highlighted)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)

# class UserList(generics.ListAPIView):
#     queryset=Snippet.objects.all()
#     serializer_class=UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer






# @api_view(['Get'])
# def api_root(request,format=None):
#     return Response({
#         'users':reverse('user-list',request=request,format=format),
#         'snippets':reverse('snippet-list',request=request,format=format)
# #     })
# class SnippetHighlight(generics.GenericAPIView):
#     queryset=Snippet.objects.all()
#     renderer_classes=[renderers.StaticHTMLRenderer]

#     def get(self,request, *args,**kwargs):
#         snippet=self.get.object()
#         return Response(snippet.highlighted)


