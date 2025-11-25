from django.db import models


class Note(models.Model):
    """
    Note model representing a user note with a title and optional content.
    """
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # set on create
    updated_at = models.DateTimeField(auto_now=True)      # set on each save

    def __str__(self) -> str:
        return f"{self.title}"
