from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout

from .forms import UserRegistrationForm

from .models import CustomUser

# predictor/views.py
from django.shortcuts import render
from .forms import LaptopPricePredictionForm
from .models import CustomUser
from .prediction import predict_laptop_price  # This should be a function in your 'prediction.py' for price prediction


def predict_price_view(request):
    predicted_price = None
    if request.method == 'POST':
        form = LaptopPricePredictionForm(request.POST)
        if form.is_valid():
            # Get data from the form
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            purchase_price = form.cleaned_data['purchase_price']
            years_used = form.cleaned_data['years_used']
            condition = form.cleaned_data['condition']
            defects = form.cleaned_data['defects']

            # Use your machine learning model or any prediction logic here
            predicted_price = predict_laptop_price(brand, model, purchase_price, years_used, condition, defects)
    else:
        form = LaptopPricePredictionForm()

    return render(request, 'predictor/predict_price.html', {'form': form, 'predicted_price': predicted_price})


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('logged_in_home')  # Redirect logged-in users to home page
    return render(request, 'predictor/landing.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if the user exists
            user = CustomUser.objects.get(username=username)
            if user.password == password:  # Compare passwords
                # Log the user in
                login(request, user)  # Using Django's login function for authentication

                # Get the 'next' parameter if it exists
                next_url = request.GET.get('next', 'logged_in_home')  # Default to logged_in_home if no 'next'
                return redirect(next_url)  # Redirect to 'next' page after successful login
            else:
                return render(request, 'predictor/login.html', {'error': 'Incorrect password'})
        except CustomUser.DoesNotExist:
            return render(request, 'predictor/login.html', {'error': 'User does not exist'})

    return render(request, 'predictor/login.html')


# Landing Page for Logged-In Users
@login_required
def logged_in_home(request):
    return render(request, 'predictor/logged_in_home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the new user
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()

    return render(request, 'predictor/register.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

