# note-keeper-46333-46342

Backend: Django + Django REST Framework

How to run
- Install dependencies:
  - pip install -r notes_app_backend/requirements.txt
- Apply migrations:
  - cd notes_app_backend
  - python manage.py migrate
- Run the development server (served on port 3001 in the environment):
  - python manage.py runserver 0.0.0.0:3001

Health endpoint
- GET /api/health/
  - 200 OK
  - {"message": "Server is up!"}

Notes API endpoints (JSON)
- Base path: /api/notes/
- List notes
  - GET /api/notes/
  - 200 OK -> [{"id":1,"title":"...","content":"...","created_at":"...","updated_at":"..."}]
- Create note
  - POST /api/notes/
  - Body:
    {
      "title": "My note",
      "content": "Optional content"
    }
  - 201 Created -> {"id":1,"title":"My note","content":"Optional content","created_at":"...","updated_at":"..."}
- Retrieve note
  - GET /api/notes/{id}/
  - 200 OK -> {"id":1,"title":"My note","content":"Optional content","created_at":"...","updated_at":"..."}
- Update note
  - PUT /api/notes/{id}/
  - Body:
    {
      "title": "Updated title",
      "content": "Updated content"
    }
  - 200 OK -> updated object
- Partial update note
  - PATCH /api/notes/{id}/
  - Body:
    {
      "title": "Only title updated"
    }
  - 200 OK -> updated object
- Delete note
  - DELETE /api/notes/{id}/
  - 204 No Content

Validation
- "title" is required and cannot be empty.

Notes
- No authentication is enforced for this sample API.
- Database uses SQLite by default (configured in settings.py).
