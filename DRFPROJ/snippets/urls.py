from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('snippets', views.SnippetViewSet,basename="snippet")
router.register('snoppetsapi',views.UserViewSet,basename='user')

# API endpoints
urlpatterns = [
    # path('', views.api_root),
    path('', include(router.urls)),
   
]