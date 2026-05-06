from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Place

@receiver([post_save, post_delete], sender=Place)
def update_project_completion_status(sender, instance, **kwargs):
    project = instance.project
    places = project.places.all()
    
    if places.exists() and all(place.is_visited for place in places):
        if not project.is_completed:
            project.is_completed = True
            project.save(update_fields=['is_completed'])
    else:
        if project.is_completed:
            project.is_completed = False
            project.save(update_fields=['is_completed'])