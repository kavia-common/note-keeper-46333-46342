from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.permissions import AllowAny

from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def health(request: Request):
    """
    Health check endpoint to verify server is running.
    Returns: JSON {"message": "Server is up!"}
    """
    return Response({"message": "Server is up!"})


class NoteViewSet(viewsets.ModelViewSet):
    """
    ViewSet providing CRUD operations for Note objects.
    Routes (via router under /api/notes/):
      - GET /api/notes/           -> list
      - POST /api/notes/          -> create
      - GET /api/notes/{id}/      -> retrieve
      - PUT /api/notes/{id}/      -> update
      - PATCH /api/notes/{id}/    -> partial_update
      - DELETE /api/notes/{id}/   -> destroy
    """
    queryset = Note.objects.all().order_by("-updated_at", "-created_at")
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]
