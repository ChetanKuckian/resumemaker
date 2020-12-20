from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from resume.api.permissions import IsOwnerOrReadOnly
from resume.models import Resume, Certificate
from resume.api.serializers import ResumeSerializer, CertificateSerializer


class ResumeViewSet(ModelViewSet):

    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Resume.objects.all()
        username = self.request.user
        print(self.request.user)
        if username is not None:
            queryset = queryset.filter(user=username)
        return queryset

    def perform_create(self, serializer):
        user_resume = self.request.user
        serializer.save(user=user_resume)


class CertificateCreateAPIView(generics.CreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def perform_create(self, serializer):
        resume_pk = self.kwargs.get("resume_pk")
        resume = generics.get_object_or_404(Resume, pk=resume_pk)
        user = self.request.user
        serializer.save(resume=resume, user=user)

    permission_classes = [IsAuthenticated]


class CertificateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
