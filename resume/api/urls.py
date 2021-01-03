from django.urls import path, include
from resume.api.views import ResumeViewSet, CertificateCreateAPIView, CertificateDetailAPIView, WorkExperienceCreateAPIView, WorkExperienceDetailAPIView, EducationCreateAPIView, EducationDetailAPIView, AchievementCreateAPIView, AchievementDetailAPIView, PersonalProjectCreateAPIView, PersonalProjectDetailAPIView, AvatarUpdateView, SkillCreateAPIView, SkillDetailAPIView, InterestCreateAPIView, InterestDetailAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"resume", ResumeViewSet, basename="resume")


urlpatterns = [
    path("", include(router.urls)),

    path('resumes/<int:resume_pk>/certificate/',
         CertificateCreateAPIView.as_view(), name="resume-certificate"),
    path('certificate/<int:pk>/', CertificateDetailAPIView.as_view(),
         name="certificate-detail"),

    path('resumes/<int:resume_pk>/workexperience/',
         WorkExperienceCreateAPIView.as_view(), name="resume-workexperience"),
    path('workexperience/<int:pk>/', WorkExperienceDetailAPIView.as_view(),
         name="workexperience-detail"),

    path('resumes/<int:resume_pk>/education/',
         EducationCreateAPIView.as_view(), name="resume-education"),
    path('education/<int:pk>/', EducationDetailAPIView.as_view(),
         name="education-detail"),

    path('resumes/<int:resume_pk>/achievement/',
         AchievementCreateAPIView.as_view(), name="resume-achievement"),
    path('achievement/<int:pk>/', AchievementDetailAPIView.as_view(),
         name="achievement-detail"),

    path('resumes/<int:resume_pk>/personalproject/',
         PersonalProjectCreateAPIView.as_view(), name="resume-personalproject"),
    path('personalproject/<int:pk>/', PersonalProjectDetailAPIView.as_view(),
         name="personalproject-detail"),

    path('resumes/<int:resume_pk>/skill/',
         SkillCreateAPIView.as_view(), name="resume-skill"),
    path('personalproject/<int:pk>/', SkillDetailAPIView.as_view(),
         name="skill-detail"),

    path('resumes/<int:resume_pk>/interest/',
         InterestCreateAPIView.as_view(), name="resume-interest"),
    path('personalproject/<int:pk>/', InterestDetailAPIView.as_view(),
         name="interest-detail"),

    path("resumes/<int:resume_pk>/avatar",
         AvatarUpdateView.as_view(), name="avatar-update"),

]
