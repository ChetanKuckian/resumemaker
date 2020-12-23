from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Resume(models.Model):
    # user = models.O(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    mobile = models.CharField(max_length=10)
    linkedin_url = models.URLField()
    github_url = models.URLField()
    skills = models.TextField(null=True)
    interests = models.TextField(null=True)
    avatar = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.id)


class Certificate(models.Model):

    certificate_name = models.CharField(max_length=150)
    certificate_date = models.DateField()
    certificate_desc = models.TextField()
    certificate_url = models.URLField(null=True)

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="certificates")

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cert_user")

    def __str__(self):
        return self.certificate_name


class WorkExperience(models.Model):

    job_title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    from_date = models.DateField()
    to_date = models.DateField()
    city_country = models.CharField(max_length=150)
    role_responsibility = models.TextField()

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="workexperiences")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="workexp_user")

    def __str__(self):
        return str(self.id)


class Education(models.Model):

    program_name = models.CharField(max_length=150)
    institute_name = models.CharField(max_length=150)
    from_date = models.DateField()
    to_date = models.DateField()
    gpa = models.CharField(max_length=10)

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="educations")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="edu_user")

    def __str__(self):
        return str(self.id)


class Achievement(models.Model):

    achievement_name = models.CharField(max_length=150)
    from_date = models.DateField()
    to_date = models.DateField()
    achievement_desc = models.TextField()

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="achievements")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="achievement_user")

    def __str__(self):
        return str(self.id)


class PersonalProject(models.Model):

    project_name = models.CharField(max_length=150)
    from_date = models.DateField()
    to_date = models.DateField()
    project_desc = models.TextField()

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="personalprojects")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="project_user")

    def __str__(self):
        return str(self.id)
