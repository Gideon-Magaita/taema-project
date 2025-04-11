from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from ckeditor.widgets import CKEditorWidget
#auth imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class SliderForm(ModelForm):
    class Meta:
        model = Slider
        fields=['title','image']

        widgets = {
            'title':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter about info','required':'required'}),
            'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class WelcomeNoteForm(ModelForm):
    class Meta:
        model = WelcomeNote
        fields=['title']
        widgets = {
            'title':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter about info','required':'required'}),
        }

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields=['title','sub_title']
        widgets = {
          'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter activity title','required':'required'}),
          'sub_title':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter activity subtitle','required':'required'}),
        }

class BoardMemberForm(ModelForm):
    class Meta:
        model = BoardMember
        fields=['name','proffesion','image']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter full name','required':'required'}),
            'proffesion':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Proffesion','required':'required'}),
            'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields=['title','status']
        widgets = {
            'title':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter about info','required':'required'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter full name','required':'required'}), 
        }

class WhoAreWeForm(ModelForm):
    class Meta:
        model = WhoAreWe
        fields=['title','description']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter description','required':'required'}),
        }

class MissionForm(ModelForm):
    class Meta:
        model = Mission
        fields=['title','description']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter description','required':'required'}),
        }


class VisionForm(ModelForm):
    class Meta:
        model = Vision
        fields=['title','description']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter description','required':'required'}),
        }


class ObjectiveForm(ModelForm):
    class Meta:
        model = Objective
        fields=['title','description']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter description','required':'required'}),
        }

class NewsForm(ModelForm):
    class Meta:
        model=News
        fields=['title','description','image','status']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter news title','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter news description','required':'required'}),
            'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }

class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        fields=['category','description','benefit']
        widgets = {
            'category':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter news title','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter news description','required':'required'}),
            'benefit':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter news description','required':'required'}),
        }

class BenefitForm(ModelForm):
    class Meta:
        model = Benefit
        fields=['description']
        widgets = {
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter news description','required':'required'}),
        }


class WorkingGroupForm(ModelForm):
    class Meta:
        model = WorkingGroup
        fields=['title','description']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a title','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter news description','required':'required'}),
        }


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields=['image','description']
        widgets = {
            'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter descriptions','required':'required'}),
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields='__all__'


class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields=['image','description']
        widgets = {
            'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter descriptions','required':'required'}),
        }


class AddressModelForm(ModelForm):
    class Meta:
        model = AddressModel
        fields=['address', 'phone_number','email']
        widgets = {
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter descriptions','required':'required'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter phone number (e.g., +255XXXXXXXXX)','required': 'required'
            }),            
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email','required':'required'}),
        }
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.startswith('+255'):
            raise forms.ValidationError("Phone number must start with +255.")
        if len(phone) != 13 or not phone[4:].isdigit():
            raise forms.ValidationError("Phone number must contain exactly 9 digits after +255.")
        return phone


class DownloadsModelForm(ModelForm):
    class Meta:
        model = Downloads
        fields=['description','file_name']
        widgets = {
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter descriptions','required':'required'}),
            'file_name':forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }