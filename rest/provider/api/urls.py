from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api', views.ItemViewSet)

# urlpatterns = [
#     path('', views.getData ),
#     path('add/', views.addItem),
#     path('update/',views.updateItem, name="update-item"),
# ]

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
