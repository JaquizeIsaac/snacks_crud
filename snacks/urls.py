from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', SnackListView.as_view(), name='snacks_list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snacks_detail'),
    path('new/', SnackCreateView.as_view(), name='snacks_create'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='snacks_update'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snacks_delete'),
]