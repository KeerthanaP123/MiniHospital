from django.db import models
from accounts.models import Account
from doctor.models import Specialization, Designation
from multiselectfield import MultiSelectField
import datetime

# Create your models here.

class Lab(models.Model):
    qualification_names = (
        ('DMLT','DMLT'), #Diploma in Medical Laboratory Technology
        ('ADMLT','ADMLT'), #Associate in Medical Laboratory Technology
        ('BMLT','BMLT'), #Bachelor of Medical Laboratory Technology
        ('MLT','MLT'), #Medical Laboratory Technology
    )

    id = models.AutoField(primary_key=True)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    year_of_service = models.IntegerField(blank=False, null=False)
    # qual_name = models.ForeignKey(Qualification, on_delete=models.CASCADE,related_name='q-realated')
    qual_name = MultiSelectField(choices=qualification_names, max_choices=5, max_length=100)
    spec_name = models.ForeignKey(Specialization, on_delete=models.CASCADE,related_name='spec_name_realted')
    des_name = models.ForeignKey(Designation, on_delete=models.CASCADE,related_name='des_name_lab')
    license_no = models.CharField(max_length=100, blank=True)
    is_doctor = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_lab = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)