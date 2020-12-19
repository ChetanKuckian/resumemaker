from django.db import models


class Resume(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    mobile = models.CharField(max_length=10)
    linkedin_url = models.URLField()
    github_url = models.URLField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Certificate(models.Model):

    certificate_name = models.CharField(max_length=150)
    certificate_date = models.DateField()
    certificate_desc = models.TextField()

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="certificates")

    def __str__(self):
        return self.certificate_name
