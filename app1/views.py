from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code

def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        country_code = request.POST.get('country_code')
        
        try:
            full_number = f"+{country_code}{phone_number}"
            parsed_number = phonenumbers.parse(full_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                messages.error(request, "Invalid phone number")
                return redirect('login')
            
            # Here you would typically generate and send OTP
            # For now, we'll just show a success message
            messages.success(request, f"OTP sent to {full_number}")
            return redirect('login')
            
        except Exception as e:
            messages.error(request, "Please enter a valid phone number")
            return redirect('login')
    
    return render(request, 'login.html')