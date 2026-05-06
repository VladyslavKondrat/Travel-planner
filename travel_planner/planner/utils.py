import requests
from django.core.cache import cache
from rest_framework.exceptions import ValidationError

def validate_external_place(external_id):
    cache_key = f"art_place_{external_id}"
    is_valid = cache.get(cache_key)
    
    if is_valid is not None:
        if not is_valid:
            raise ValidationError(f"Place with external_id {external_id} does not exist.")
        return True

    url = f"https://api.artic.edu/api/v1/artworks/{external_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        cache.set(cache_key, True, timeout=86400)
        return True
    else:
        cache.set(cache_key, False, timeout=86400)
        raise ValidationError(f"Place with external_id {external_id} does not exist in the Art Institute API.")