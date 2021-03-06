from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import PermissionDenied
from resume.api.permissions import IsOwnerOrReadOnly, IsRelatedToUser
from resume.models import Resume, Certificate, WorkExperience, Education, Achievement, PersonalProject, Skill, Interest
from resume.api.serializers import ResumeSerializer, CertificateSerializer, WorkExperienceSerializer, EducationSerializer, AchievementSerializer, PersonalProjectSerializer, ResumeAvaatarSerializer, SkillSerializer, InterestSerializer


# Resume model viewsets

class ResumeViewSet(ModelViewSet):

    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        username = self.request.user
        if username is not None:
            queryset = Resume.objects.filter(user=username)
        else:
            raise PermissionDenied()

        return queryset

    def perform_create(self, serializer):
        user_resume = self.request.user
        serializer.save(user=user_resume)


# Certificate model viewsets

class CertificateCreateAPIView(generics.CreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        resume_pk = self.kwargs.get("resume_pk")
        resume = generics.get_object_or_404(Resume, pk=resume_pk)
        user = resume.user
        if user == self.request.user:
            serializer.save(resume=resume)
        else:
            raise PermissionDenied()


class CertificateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated, IsRelatedToUser]


# WorkExperience model viewsets

class WorkExperienceCreateAPIView(generics.CreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

    def perform_create(self, serializer):
        resume_pk = self.kwargs.get("resume_pk")
        resume = generics.get_object_or_404(Resume, pk=resume_pk)
        user = resume.user
        if user == self.request.user:
            serializer.save(resume=resume)
        else:
            raise PermissionDenied()

    permission_classes = [IsAuthenticated]


class WorkExperienceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

    permission_classes = [IsAuthenticated, IsRelatedToUser]


# Education model viewsets

class EducationCreateAPIView(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def perform_create(self, serializer):
        resume_pk = self.kwargs.get("resume_pk")
        resume = generics.get_object_or_404(Resume, pk=resume_pk)
        user = resume.user
        if user == self.request.user:
            serializer.save(resume=resume)
        else:
            raise PermissionDenied()

    permission_classes = [IsAuthenticated]


class EducationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    permission_classes = [IsAuthenticated, IsRelatedToUser]


# Achievement model viewsets

class AchievementCreateAPIView(generics.CreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    def perform_create(self, serializer):
        resume_pk = self.kwargs.get("resume_pk")
        resume = generics.get_object_or_404(Resume, pk=resume_pk)
        user = resume.user
        if user == self.request.user:
            serializer.save(resume=resume)
        else:
            raise PermissionDenied()

    permission_classes = [IsAuthenticated]


class AchievementDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    permission_classes = [IsAuthenticated, IsRelatedToUser]


# PersonalProject model viewsets

class PersonalProjectCreateAPIView(generics.CreateAPIView):
    queryset = PersonalProject.objects.all()
    serializer_class = PersonalProjectSerializer

    def perform_create(self, serializer):
        resume_pk = self.kwargs.get("resume_pk")
        resume = generics.get_object_or_404(Resume, pk=resume_pk)
        user = resume.user
        if user == self.request.user:
            serializer.save(resume=resume)
        else:
            raise PermissionDenied()

    permission_classes = [IsAuthenticated]


class PersonalProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalProject.objects.all()
    serializer_class = PersonalProjectSerializer

    permission_classes = [IsAuthenticated, IsRelatedToUser]


# Resume Image update View

class AvatarUpdateView(generics.UpdateAPIView):

    serializer_class = ResumeAvaatarSerializer
    permission_classes = [IsAuthenticated, IsRelatedToUser]

    def get_object(self):
        resume_pk = self.kwargs.get("resume_pk")
        resume = generics.get_object_or_404(Resume, pk=resume_pk)
        return resume


# Skill model viewsets

class SkillCreateAPIView(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def perform_create(self, serializer):
        resume_pk = self.kwargs.get("resume_pk")
        resume = generics.get_object_or_404(Resume, pk=resume_pk)
        user = resume.user
        if user == self.request.user:
            serializer.save(resume=resume)
        else:
            raise PermissionDenied()

    permission_classes = [IsAuthenticated]


class SkillDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    permission_classes = [IsAuthenticated, IsRelatedToUser]


# Interest model viewsets

class InterestCreateAPIView(generics.CreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

    def perform_create(self, serializer):
        resume_pk = self.kwargs.get("resume_pk")
        resume = generics.get_object_or_404(Resume, pk=resume_pk)
        user = resume.user
        if user == self.request.user:
            serializer.save(resume=resume)
        else:
            raise PermissionDenied()

    permission_classes = [IsAuthenticated]


class InterestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

    permission_classes = [IsAuthenticated, IsRelatedToUser]
