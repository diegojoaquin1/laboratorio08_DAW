from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrganizerViewSet, TeamViewSet, PlayerViewSet,
    TournamentViewSet, PlayerTournamentViewSet
)

router = DefaultRouter()
router.register(r'organizers', OrganizerViewSet, basename='organizer')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'tournaments', TournamentViewSet, basename='tournament')
router.register(r'player-tournaments', PlayerTournamentViewSet, basename='player-tournament')

urlpatterns = [
    path('', include(router.urls)),
]
