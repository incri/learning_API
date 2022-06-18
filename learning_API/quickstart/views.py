from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]