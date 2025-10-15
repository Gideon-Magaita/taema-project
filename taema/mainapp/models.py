from encodings.punycode import T
from sre_parse import CATEGORIES
from tkinter.tix import Tree
from turtle import mode
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator
#Home page models.
class Slider(models.Model):
    title = RichTextField()
    image = models.ImageField(max_length=200,upload_to='images/')

    def __str__(self):
        return self.title
    

class WelcomeNote(models.Model):
    image = models.ImageField(max_length=200,upload_to='images/',null=True,blank=True)
    title = RichTextField()

    def __str__(self):
        return self.title
    

class Activity(models.Model):
    title = models.CharField(max_length=200)
    sub_title = RichTextField()

    def __str__(self):
        return self.title
    

class BoardMember(models.Model):
    name = models.CharField(max_length=200)
    proffesion = models.CharField(max_length=200)
    image = models.ImageField(max_length=200,upload_to='images/')

    def __str__(self):
        return self.name
    

STATUS_CHOICES=(
   ('publish','publish'),
   ('unpublish','unpublish'),
)

class Comment(models.Model):
    title = RichTextField()
    status = models.CharField(max_length=200,choices=STATUS_CHOICES,default='publish')

    def __str__(self):
        return self.title

#about page models
class WhoAreWe(models.Model):
    image = models.ImageField(max_length=200,blank=True,null=True,upload_to='images/')
    title = models.CharField(max_length=200,default='Who Are We')
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Mission(models.Model):
    image = models.ImageField(max_length=200,blank=True,null=True,upload_to='images/')
    title = models.CharField(max_length=200,default='Mission')
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Vision(models.Model):
    image = models.ImageField(max_length=200,blank=True,null=True,upload_to='images/')
    title = models.CharField(max_length=200,default='Vision')
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Objective(models.Model):
    image = models.ImageField(max_length=200,blank=True,null=True,upload_to='images/')
    title = models.CharField(max_length=200,default='Objectives')
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

#News and updates

NEWS_STATUS=(
    ('publish','publish'),
    ('unpublish','unpublish'),
)
class News(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(max_length=200,upload_to='images/')
    status = models.CharField(max_length=200,choices=NEWS_STATUS,default='publish')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
############ Other Models #########
class Membership(models.Model):
    category = models.CharField(max_length=200)
    description = RichTextField()
    benefit = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category


class Benefit(models.Model):
    image = models.ImageField(max_length=200, upload_to='images/', null=True, blank=True, default='')
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description



class WorkingGroup(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    image = models.ImageField(max_length=200,upload_to='images/')
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description

class Partner(models.Model):
    image = models.ImageField(max_length=200,upload_to='images/')
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email
    

class AddressModel(models.Model):
    address = RichTextField()
    phone_number = models.CharField(
        max_length=13, 
        validators=[
            RegexValidator(
                regex=r'^\+255[0-9]{9}$',
                message="Phone number must start with +255 followed by 9 digits."
            )
        ]
    )
    email = models.EmailField(max_length=200)

    def __str__(self):
     return f"{self.address} - {self.phone_number} - {self.email}"
    

#Models to count the number of visitors
class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address


class Downloads(models.Model):
    description = models.CharField(max_length=200)
    file_name = models.FileField(max_length=200,upload_to='images/')
    # date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description

######Individual Membership######
class Specialization(models.Model):
    area_name = models.CharField(max_length=200)

    def __str__(self):
        return self.area_name
FEE_CHOICES = [
    ('Tsh.0', 'Tsh.0'),
]

ANNUAL_FEE_CHOICES = [
    ('Tsh.0 1 Year', 'Tsh.0 1 Year'),
    ('Tsh.0 2 Year', 'Tsh.0 2 Year'),
]
Agree=[
    ('yes','Yes'),
    ('no','No'),
]
class Individual(models.Model):
    full_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email  = models.EmailField(max_length=200)
    mobile_number = models.CharField(max_length=13)
    id_number = models.CharField(max_length=20)
    area_of_specialization = models.ForeignKey(Specialization,on_delete=models.CASCADE,blank=Tree,null=True)
    name_of_the_organization = models.CharField(max_length=200)
    number_of_year_of_experience_in_emobility_sector = models.IntegerField()
    registration_fee = models.CharField(max_length=20,choices=FEE_CHOICES)
    annual_membership_subscription = models.CharField(max_length=20,choices=ANNUAL_FEE_CHOICES)
    describe_your_contribution = models.TextField()
    what_are_the_individual_expectations= models.TextField()
    i_agree = models.CharField(max_length=20,choices=Agree)
    introduce = models.CharField(max_length=20,choices=Agree)

    def __str__(self):
        return self.full_name



######Organization Membership######
class CategoryModel(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class CategoryMembership(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


TERMS=[
    ('yes','yes'),
    ('no','no'),
]

class Organization(models.Model):
    organization_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email  = models.EmailField(max_length=200)
    mobile_number = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    category = models.ManyToManyField(CategoryModel)
    number_of_existing_employees = models.IntegerField()
    name_of_the_organization_representative = models.CharField(max_length=200)
    email_the_representative  = models.EmailField(max_length=200)
    mobile_number_of_representative = models.CharField(max_length=13)
    describe_the_motivation_to_join_the_association= models.TextField()
    organization_expectations = models.TextField(default=None)
    upload_Company_Profile = models.FileField(upload_to='images/')
    membership_Category = models.ManyToManyField(CategoryMembership)
    terms_and_constitution_of_the_organization = models.CharField(max_length=200,choices=TERMS)


    def __str__(self):
        return self.organization_name

class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name