from rest_framework import generics
from snacks_api.models import Snack
from .serializers import SnackSerializer
from .permissions import OwnerOrReadOnly, CreateOrReadOnly


class SnacksListAPIView(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (CreateOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class SnacksDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (OwnerOrReadOnly,)