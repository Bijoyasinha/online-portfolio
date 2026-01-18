from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()  # percentage

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)
    def __str__(self):
        return self.title
    
class Experience(models.Model):
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    duration = models.CharField(max_length=50) 
    description = models.TextField()

    def _str_(self):
        return f"{self.position} at {self.company}"

# ৩. Social Links সেকশন
class SocialLink(models.Model):
    platform = models.CharField(max_length=50) 
    url = models.URLField()

    def _str_(self):
        return self.platform

# ৪. Services সেকশন
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.title 
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_designation = models.CharField(max_length=100) # যেমন: CEO, ABC Tech
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True)

    def __str__(self):
        return self.client_name
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='blog_thumbs/')

    def __str__(self):
        return self.title     

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    certificate_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
class Achievement(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title  