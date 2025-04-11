from encodings.punycode import T
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
    title = models.CharField(max_length=200,default='Who Are We')
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Mission(models.Model):
    title = models.CharField(max_length=200,default='Mission')
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Vision(models.Model):
    title = models.CharField(max_length=200,default='Vision')
    description = RichTextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Objective(models.Model):
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