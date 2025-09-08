from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([
    Slider,
    WelcomeNote,
    Activity,
    BoardMember,
    Comment,
    WhoAreWe,
    Mission,
    Vision,
    Objective,
    Membership,
    Benefit,
    WorkingGroup,
    Gallery,
    Partner,
    Contact,
    Visitor,
    Downloads,
    Specialization,
    Individual,
    Organization,
    CategoryModel,
    CategoryMembership
])
