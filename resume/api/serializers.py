from rest_framework import serializers
from resume.models import Certificate, Resume


class CertificateSerializer(serializers.ModelSerializer):

    # review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Certificate
        exclude = ("resume",)


class ResumeSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"
