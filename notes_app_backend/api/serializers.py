from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Note model with simple validation to ensure title is present and non-empty.
    """

    # PUBLIC_INTERFACE
    class Meta:
        """This serializer exposes Note fields for API read/write."""
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    # PUBLIC_INTERFACE
    def validate_title(self, value: str) -> str:
        """Ensure title is present and not empty/whitespace."""
        if value is None or not str(value).strip():
            raise serializers.ValidationError("Title is required and cannot be empty.")
        return value.strip()
