from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    phone_number = PhoneNumberField(region='IN')  # Default region, can be changed
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return str(self.phone_number)
    




# models.py
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('company', 'Company'),
    ]
    
    company_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = PhoneNumberField(region='IN')
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='individual'  # <- This line avoids the error
    )
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return str(self.phone_number)