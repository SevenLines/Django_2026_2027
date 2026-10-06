from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings

from marks.api import DisciplineViewSet, GroupViewSet, LessonViewSet, MarkViewSet
from marks.views import GroupListView

router = DefaultRouter()
router.register('groups', GroupViewSet, 'groups')
router.register('lessons', LessonViewSet, 'lessons')
router.register('disciplines', DisciplineViewSet, 'disciplines')
router.register('marks', MarkViewSet, 'marks')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
