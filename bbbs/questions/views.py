from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .serializers import QuestionSerializer, TagSerializer
from .models import Question, Tag


class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TagSerializer
    pagination_class = PageNumberPagination
    queryset = Tag.objects.all()


class QuestionListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class CreateUpdateViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    pass


class QuestionCreateViewSet(CreateUpdateViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated, ]
