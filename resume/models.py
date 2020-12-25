from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField()
    mobile = models.CharField(max_length=10, null=True)
    linkedin_url = models.URLField(null=True)
    github_url = models.URLField(null=True)
    designation = models.CharField(max_length=50)
    summary = models.CharField(max_length=300)
    skills = models.TextField(null=True)
    interests = models.TextField(null=True)
    avatar = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.id)


class Certificate(models.Model):

    certificate_name = models.CharField(max_length=150)
    certificate_date = models.DateField(null=True)
    certificate_desc = models.TextField(null=True)
    certificate_url = models.URLField(null=True)

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="certificates")

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cert_user")

    def __str__(self):
        return self.certificate_name


class WorkExperience(models.Model):

    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=90)
    from_date = models.DateField()
    to_date = models.DateField(null=True)
    city_country = models.CharField(max_length=100, null=True)
    role_responsibility = models.TextField()

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="workexperiences")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="workexp_user")

    def __str__(self):
        return str(self.id)


class Education(models.Model):

    program_name = models.CharField(max_length=60)
    institute_name = models.CharField(max_length=60)
    from_date = models.DateField()
    to_date = models.DateField(null=True)
    gpa = models.CharField(max_length=10, null=True)

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="educations")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="edu_user")

    def __str__(self):
        return str(self.id)


class Achievement(models.Model):

    achievement_name = models.CharField(max_length=100)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    achievement_desc = models.TextField(null=True)

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="achievements")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="achievement_user")

    def __str__(self):
        return str(self.id)


class PersonalProject(models.Model):

    project_name = models.CharField(max_length=100)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    project_desc = models.TextField()
    project_url = models.URLField(null=True)

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="personalprojects")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="project_user")

    def __str__(self):
        return str(self.id)
