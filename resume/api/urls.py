from django.urls import path, include
from resume.api.views import ResumeViewSet, CertificateCreateAPIView, CertificateDetailAPIView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"resume", ResumeViewSet, basename="resume")

urlpatterns = [
    path("", include(router.urls)),
    path('resumes/<int:resume_pk>/certificate/',
         CertificateCreateAPIView.as_view(), name="resume-certificate"),
    path('certificate/<int:pk>/', CertificateDetailAPIView.as_view(),
         name="certificate-detail")

]
