from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from marks.models import Discipline, Group, Lesson, Mark
from marks.serializers import DisciplineSerializer, GroupSerializer, LessonSerializer, MarkSerializer

class GroupViewSet(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LessonViewSet(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class DisciplineViewSet(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class MarkViewSet(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer