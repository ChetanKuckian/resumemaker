from rest_framework import generics
from rest_framework.exceptions import ValidationError

from resume.models import Resume, Certificate
from resume.api.serializers import ResumeSerializer, CertificateSerializer


class ResumeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Resume.objects.all().order_by("id")
    serializer_class = ResumeSerializer
    # permission_classes = [IsAdminUserorReadOnly]
    # pagination_class = SmallSetPagination


class ResumeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    # permission_classes = [IsAdminUserorReadOnly]


class CertificateCreateAPIView(generics.CreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        resume_pk = self.kwargs.get("resume_pk")
        resume = generics.get_object_or_404(Resume, pk=resume_pk)
        # review_author = self.request.user

        #certificate_queryset = Certificate.objects.filter(resume=resume)

        # if review_queryset.exists():
        #     raise ValidationError("You Have ALready Reviewd This Ebook!")

        serializer.save(resume=resume)


class CertificateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    # permission_classes = [IsReviewAuthorOrReadOnly]
