from rest_framework import serializers
from resume.models import Certificate, Resume


class CertificateSerializer(serializers.ModelSerializer):

    # review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Certificate
        # exclude = ("resume",)
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    certificate = CertificateSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"
