from rest_framework import viewsets
from .models import Content, Comment, Like, Playlist
from .serializers import CommentSerializer, ContentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    #def perform_create(self, serializer):
     #   serializer.save(creator=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)