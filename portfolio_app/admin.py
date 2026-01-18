from django.contrib import admin
from .models import Achievement, Experience, Service, SocialLink, Testimonial, Blog, Certificate, Profile, Skill, Project

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Certificate)
admin.site.register(Achievement)
admin.site.register(Experience)
admin.site.register(SocialLink)