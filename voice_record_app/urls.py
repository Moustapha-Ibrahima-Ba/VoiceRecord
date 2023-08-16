from django.urls import path
from .views import (
    AudioListView, AudioDetailView, AudioCreateView, AudioUpdateView, AudioDeleteView,
    DomaineListView, DomaineDetailView, DomaineCreateView, DomaineUpdateView, DomaineDeleteView,
)

urlpatterns = [
    # URLs pour l'entité "audio"
    path('', AudioListView.as_view(), name='audio_list'),
    path('audio/<int:pk>/', AudioDetailView.as_view(), name='audio_detail'),
    path('audio/create/', AudioCreateView.as_view(), name='audio_create'),
    path('audio/update/<int:pk>/', AudioUpdateView.as_view(), name='audio_update'),
    path('audio/delete/<int:pk>/', AudioDeleteView.as_view(), name='audio_delete'),
    
    # URLs pour l'entité "domaine",
    path('domaine/', DomaineListView.as_view(), name='domaine_list'),
    path('domaine/<int:pk>/', DomaineDetailView.as_view(), name='domaine_detail'),
    path('domaine/create/', DomaineCreateView.as_view(), name='domaine_create'),
    path('domaine/update/<int:pk>/', DomaineUpdateView.as_view(), name='domaine_update'),
    path('domaine/delete/<int:pk>/', DomaineDeleteView.as_view(), name='domaine_delete'),
]
