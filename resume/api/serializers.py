from rest_framework import serializers
from resume.models import Resume, Certificate, WorkExperience, Education, Achievement, PersonalProject


class CertificateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    resume = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Certificate
        # exclude = ("resume",)
        fields = "__all__"


class WorkExperienceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    resume = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = WorkExperience
        # exclude = ("resume",)
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    resume = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Education
        # exclude = ("resume",)
        fields = "__all__"


class AchievementSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    resume = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Achievement
        # exclude = ("resume",)
        fields = "__all__"


class PersonalProjectSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    resume = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PersonalProject
        # exclude = ("resume",)
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    certificates = CertificateSerializer(many=True, read_only=True)
    workexperiences = WorkExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, read_only=True)
    personalprojects = PersonalProjectSerializer(many=True, read_only=True)
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"

    def validate_mobile(self, value):
        if len(value) != 10:
            raise serializers.ValidationError(
                'Mobile Number Should be of 10 digits')
        else:
            if not value.isnumeric():
                raise serializers.ValidationError(
                    'Please Provide Only Numbers in Mobile')


class ResumeAvaatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ("avatar",)
