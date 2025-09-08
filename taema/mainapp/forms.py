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
        fields=['image','title']
        widgets = {
            'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
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
        fields=['image','title','description']
        widgets={
            'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter description','required':'required'}),
        }

class MissionForm(ModelForm):
    class Meta:
        model = Mission
        fields=['image','title','description']
        widgets={
            'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter description','required':'required'}),
        }


class VisionForm(ModelForm):
    class Meta:
        model = Vision
        fields=['image','title','description']
        widgets={
            'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter description','required':'required'}),
        }


class ObjectiveForm(ModelForm):
    class Meta:
        model = Objective
        fields=['image','title','description']
        widgets={
            'image':forms.ClearableFileInput(attrs={'class': 'form-control'}),
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

###Membership Forms###
class SpecializationForm(ModelForm):
    class Meta:
        model = Specialization
        fields=['area_name']

        widgets={
                'area_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter area of specialization','required':'required'}),
        }


class IndividualForm(forms.ModelForm):
    class Meta:
        model  = Individual
        fields = [
            "full_name",
            "city",
            "email",
            "mobile_number",
            "id_number",
            "area_of_specialization",
            "name_of_the_organization",
            "number_of_year_of_experience_in_emobility_sector",
            "registration_fee",
            "annual_membership_subscription",
            "describe_your_contribution",
            "what_are_the_individual_expectations",
            "i_agree",
            "introduce",
        ]

        widgets = {
            # text fields
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter full name",
                    "required": "required",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter city",
                    "required": "required",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter email address",
                    "required": "required",
                }
            ),
            "mobile_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter mobile number (e.g. +255…)",
                    "required": "required",
                }
            ),
            "id_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter national ID / passport number",
                    "required": "required",
                }
            ),
            "name_of_the_organization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Organization name",
                    "required": "required",
                }
            ),

            # ForeignKey → select box
            "area_of_specialization": forms.Select(
                attrs={
                    "class": "form-select",
                    "required": "required",
                }
            ),

            # integer field
            "number_of_year_of_experience_in_emobility_sector": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Years of experience",
                    "min": 0,
                    "step": 1,
                    "required": "required",
                }
            ),

            # choice fields rendered as radio buttons
            "registration_fee": forms.RadioSelect(
                choices=FEE_CHOICES,
                attrs={"class": "form-check-input"}
            ),
            "annual_membership_subscription": forms.RadioSelect(
                choices=ANNUAL_FEE_CHOICES,
                attrs={"class": "form-check-input"}
            ),
            "i_agree": forms.RadioSelect(
                choices=Agree,
                attrs={"class": "form-check-input"}
            ),
            "introduce": forms.RadioSelect(
                choices=Agree,
                attrs={"class": "form-check-input"}
            ),

            # long‑text areas
            "describe_your_contribution": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Describe your contribution to the e‑mobility sector …",
                    "rows": 4,
                    "required": "required",
                }
            ),
            "what_are_the_individual_expectations": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "What do you expect from the association …",
                    "rows": 4,
                    "required": "required",
                }
            ),
        }



class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            "organization_name",
            "city",
            "email",
            "mobile_number",
            "address",
            "category",
            "number_of_existing_employees",
            "name_of_the_organization_representative",
            "email_the_representative",
            "mobile_number_of_representative",
            "describe_the_motivation_to_join_the_association",
            "what_are_the_organization_expectations_once_you_join_the_association",
            "upload_Company_Profile",
            "membership_Category",
            "terms_and_constitution_of_the_organization",
        ]

        widgets = {
            "organization_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter organization name",
                "required": "required",
            }),
            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter city",
                "required": "required",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter organization email",
                "required": "required",
            }),
            "mobile_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter organization mobile number (e.g. +255…) ",
                "required": "required",
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter address",
                "required": "required",
            }),
            "category": forms.CheckboxSelectMultiple(attrs={
                "class": "form-check-input",
            }),
            "number_of_existing_employees": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter number of employees",
                "min": 0,
                "step": 1,
                "required": "required",
            }),
            "name_of_the_organization_representative": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Representative's full name",
                "required": "required",
            }),
            "email_the_representative": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Representative's email",
                "required": "required",
            }),
            "mobile_number_of_representative": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Representative's mobile number",
                "required": "required",
            }),
            "describe_the_motivation_to_join_the_association": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Describe your motivation for joining the association…",
                "rows": 4,
                "required": "required",
            }),
            "what_are_the_organization_expectations_once_you_join_the_association": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "What does your organization expect from the association?",
                "rows": 4,
                "required": "required",
            }),
            "upload_Company_Profile": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "required": "required",
            }),
            "membership_Category": forms.CheckboxSelectMultiple(attrs={
                "class": "form-check-input",
            }),
            "terms_and_constitution_of_the_organization": forms.RadioSelect(attrs={
                "class": "form-check-input",
            }),
        }