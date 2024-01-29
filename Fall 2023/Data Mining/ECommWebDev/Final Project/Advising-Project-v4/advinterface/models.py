# advinterface/models.py
from django.db import models

class CommunicationClass(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
      return f"{self.code} - {self.name}"

class MathematicsClass(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
      return f"{self.code} - {self.name}"

class SocialSciencesClass(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
      return f"{self.code} - {self.name}"

class ComponentAreaClass(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
      return f"{self.code} - {self.name}"

class CISClass(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
      return f"{self.code} - {self.name}"

class AdvancedCISElective(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
      return f"{self.code} - {self.name}"

class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    buff_id = models.CharField(max_length=7)
    email = models.EmailField()

    # Communication Classes
    communication_classes = models.ManyToManyField(
        CommunicationClass, related_name='communication_classes', blank=True
    )

    # Mathematics Class
    mathematics_class = models.ForeignKey(
        MathematicsClass, related_name='mathematics_class', on_delete=models.SET_NULL, null=True, blank=True
    )

    # Social Sciences Class
    social_sciences_class = models.ForeignKey(
        SocialSciencesClass, related_name='social_sciences_class', on_delete=models.SET_NULL, null=True, blank=True
    )

    # Component Area Classes
    component_area_classes = models.ManyToManyField(
        ComponentAreaClass, related_name='component_area_classes', blank=True
    )

    # CIS Classes
    cis_classes = models.ManyToManyField(CISClass, related_name='cis_classes', blank=True)

    # 9 HOURS FROM Classes
    advanced_cis_electives = models.ManyToManyField(
        AdvancedCISElective, related_name='advanced_cis_electives', blank=True
    )

    # Transcript Upload
    transcript_upload = models.FileField(upload_to='transcripts/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.buff_id})"
