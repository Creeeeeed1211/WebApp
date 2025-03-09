from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Professor, Module, ModuleInstance, Rating
from .serializers import ProfessorSerializer, ModuleSerializer, ModuleInstanceSerializer, RatingSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleInstanceViewSet(viewsets.ModelViewSet):
    queryset = ModuleInstance.objects.all()
    serializer_class = ModuleInstanceSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]  # Requires login

    def perform_create(self, serializer):
        print(f"DEBUG: Current request.user -> {self.request.user}")  # Debugging line
        print(f"DEBUG: Is user authenticated? {self.request.user.is_authenticated}")  # New Debugging line
        serializer.save(user=self.request.user)  # Automatically assign logged-in user

