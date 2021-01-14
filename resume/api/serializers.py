from rest_framework import serializers
from resume.models import Resume, Certificate, WorkExperience, Education, Achievement, PersonalProject, Skill, Interest


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        exclude = ("resume",)


class WorkExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkExperience
        exclude = ("resume",)


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        exclude = ("resume",)


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        exclude = ("resume",)


class PersonalProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalProject
        exclude = ("resume",)


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        exclude = ("resume",)


class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        exclude = ("resume",)


class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    certificates = CertificateSerializer(many=True, read_only=True)
    workexperiences = WorkExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, read_only=True)
    personalprojects = PersonalProjectSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    interests = InterestSerializer(many=True, read_only=True)
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
        return value


class ResumeAvaatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ("avatar",)
