from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code
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








def register_view(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        phone_number = request.POST.get('phone_number')
        country_code = request.POST.get('country_code')
        user_type = request.POST.get('user_type')
        
        try:
            full_number = f"+{country_code}{phone_number}"
            parsed_number = phonenumbers.parse(full_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                messages.error(request, "Invalid phone number")
                return redirect('register')
            
            # Check if user already exists
            if UserProfile.objects.filter(phone_number=full_number).exists():
                messages.error(request, "User with this phone number already exists")
                return redirect('register')
            
            # Create new user
            UserProfile.objects.create(
                company_name=company_name if user_type == 'company' else None,
                phone_number=full_number,
                user_type=user_type
            )
            
            messages.success(request, "Registration successful! Please login.")
            return redirect('register')
            
        except Exception as e:
            messages.error(request, "Registration failed. Please try again.")
            return redirect('register')
    
    return render(request, 'registration.html')





def index(request):
    return render(request, 'index.html')

def wishlist(request):
    return render(request, 'wishlist.html')