from rest_framework import serializers
from resume.models import Resume, Certificate


class CertificateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    resume = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Certificate
        # exclude = ("resume",)
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    certificates = CertificateSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"
