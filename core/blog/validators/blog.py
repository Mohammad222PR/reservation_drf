import os
from django.core.exceptions import ValidationError


# __Blog_validation__#
def validate_blog_title(value):
    if value <= str(5):
        raise ValidationError("title cannot smaller than 5 characters")


def validate_blog_content(value):
    if value <= str(30):
        raise ValidationError("title cannot smaller than 30 characters")


def validate_blog_slug(value):
    if value <= str(5):
        raise ValidationError("slug cannot smaller than 5 characters")


def validate_file_image(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".jpg", ".png"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")


# __Category_validation__#
def validate_category_title(value):
    if value <= str(5):
        raise ValidationError("title cannot smaller than 5 characters")


# __Tag_validation__#
def validate_tag_title(value):
    if value <= str(5):
        raise ValidationError("title cannot smaller than 5 characters")
