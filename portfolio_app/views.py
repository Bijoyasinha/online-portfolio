from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Skill, Project, Experience, SocialLink, Service, Testimonial, Blog, Certificate, Achievement

# ১. হোম পেজ ভিউ
def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.all()
    certificates = Certificate.objects.all()
    achievements = Achievement.objects.all()
    social_links = SocialLink.objects.all()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'services': services,
        'testimonials': testimonials,
        'blogs': blogs,
        'certificates': certificates,
        'achievements': achievements,
        'social_links': social_links,
    }
    return render(request, 'home.html', context)

# ২. লগইন ভিউ
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# ৩. লগআউট ভিউ
def logout_view(request):
    logout(request)
    return redirect('home')