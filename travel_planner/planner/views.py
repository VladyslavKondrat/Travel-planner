from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, Place
from .serializers import ProjectSerializer, PlaceSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().prefetch_related('places')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_completed']

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        if project.places.filter(is_visited=True).exists():
            return Response(
                {"detail": "Cannot delete project because it contains visited places."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        #/api/projects/{project_pk}/places/
        return Place.objects.filter(project_id=self.kwargs['project_pk'])

    def perform_create(self, serializer):
        project_id = self.kwargs['project_pk']
        current_places_count = Place.objects.filter(project_id=project_id).count()
        
        
        if current_places_count >= 10:
            from rest_framework.exceptions import ValidationError
            raise ValidationError({"detail": "This project already has the maximum of 10 places."})
            
        serializer.save(project_id=project_id)
