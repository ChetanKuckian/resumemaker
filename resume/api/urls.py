from django.urls import path
from resume.api.views import ResumeListCreateAPIView, ResumeDetailAPIView, CertificateCreateAPIView, CertificateDetailAPIView


urlpatterns = [
    path('resume/', ResumeListCreateAPIView.as_view(), name="resume-list"),
    path('resume/<int:pk>/', ResumeDetailAPIView.as_view(), name="resume-detail"),
    path('resume/<int:resume_pk>/certificate/',
         CertificateCreateAPIView.as_view(), name="resume-certificate"),
    path('certificate/<int:pk>/', CertificateDetailAPIView.as_view(),
         name="certificate-detail")
]
