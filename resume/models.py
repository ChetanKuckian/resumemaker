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
        return str(self.user.username) + str(self.id)


class Certificate(models.Model):

    certificate_name = models.CharField(max_length=150)
    certificate_date = models.DateField()
    certificate_desc = models.TextField()

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,
                               related_name="certificates")

    def __str__(self):
        return self.certificate_name
