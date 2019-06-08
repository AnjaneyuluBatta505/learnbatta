from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('student-viewset', views.StudentViewSet, basename='student_vs')
router.register('student-generic-viewset', views.StudentGenericViewSet, basename='student_gvs')
router.register('student-model-viewset', views.StudentModelViewSet, basename='student_mvs')
urlpatterns = router.urls
print(urlpatterns)