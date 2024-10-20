from django.core.exceptions import ValidationError


def validate_file_size(image_object):
    if image_object.size > 5 * 1024 * 1024:
        raise ValidationError('The maximum file size allowed is 5MB')