from rest_framework import viewsets

from .serializer import DocumentSerializer
from .models import Document


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
