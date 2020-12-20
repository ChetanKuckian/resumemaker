from django.contrib import admin
from resume.models import Certificate, Resume, WorkExperience, Education, Achievement, PersonalProject
# Register your models here.
admin.site.register(Resume)
admin.site.register(Certificate)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Achievement)
admin.site.register(PersonalProject)
