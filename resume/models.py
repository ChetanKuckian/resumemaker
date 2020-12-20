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

    def __str__(self):
        return str(self.id)


class Certificate(models.Model):

    certificate_name = models.CharField(max_length=150)
    certificate_date = models.DateField()
    certificate_desc = models.TextField()
    certificate_url = models.URLField()

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="certi_resume")

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

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="workexp_resume")

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
                               related_name="edu_resume")

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
                               related_name="achievement_resume")

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="achievement_user")

    def __str__(self):
        return str(self.id)
