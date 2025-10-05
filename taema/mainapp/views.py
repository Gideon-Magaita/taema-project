from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
#Counting visitors
from django.utils.timezone import now
# Create your views here.

def get_client_ip(request):
    """Retrieve client IP address."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    news_list = News.objects.all().order_by('-date')  # Order by latest news first
    paginator = Paginator(news_list,3)  # Show 3 news items per page

    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)

    """Home page for the front-end website with daily visitor tracking."""
    slide = Slider.objects.all()
    note = WelcomeNote.objects.all()
    activity = Activity.objects.all()
    member = BoardMember.objects.all()
    comment = Comment.objects.filter(status='publish')
    news = News.objects.all()
    address = AddressModel.objects.all()

    # Track visitor per day
    ip = get_client_ip(request)
    today = now().date()

    if not Visitor.objects.filter(ip_address=ip, visit_time__date=today).exists():
        Visitor.objects.create(ip_address=ip)

    context = {
        'slide': slide,
        'note': note,
        'activity': activity,
        'member': member,
        'comment': comment,
        'news':news_page,
        'address':address,
    }
    return render(request, 'pages/users/home.html', context)



def main_view(request):
    address = AddressModel.objects.all()
    contact_info = AddressModel.objects.all()
    return render(request, 'pages/users/main.html', {'contact_info': contact_info,'address':address,})



def news(request):
    address = AddressModel.objects.all()
    news_list = News.objects.all().order_by('-date')  # Order by latest news first
    paginator = Paginator(news_list, 6)  # Show 6 news items per page

    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)

    context = {
        'news': news_page,
        'address':address,
    }
    return render(request, 'pages/users/news.html', context)



def news_details(request,id):
    address = AddressModel.objects.all()
    news = News.objects.get(id=id)
    return render(request,'pages/users/news-details.html',{'news':news,'address':address,})



def about(request):
    who = WhoAreWe.objects.all()
    content = Mission.objects.all()
    vision = Vision.objects.all()
    objective = Objective.objects.all()
    address = AddressModel.objects.all()
    team = TeamMember.objects.all()

    context={
        'who':who,
        'content':content,
        'vision':vision,
        'objective':objective,
        'address':address,
        'team':team,
    }
    return render(request,'pages/users/about.html',context)


def contact(request):
    address = AddressModel.objects.all()
    address = AddressModel.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Message sent successfully')
            return redirect('contact')
        else:
            messages.error(request,'something went wrong')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form,
        'address':address,
        'address':address,
    }
    return render(request,'pages/users/contact.html',context)




def works(request):
    address = AddressModel.objects.all()
    context={
        'address':address
    }
    return render(request,'pages/users/works.html',context)



def working_groups(request):
    work = WorkingGroup.objects.all()
    address = AddressModel.objects.all()
    return render(request,'pages/users/working-group.html',{'work':work,'address':address})


def photo_gall(request):
    gall = Gallery.objects.all()
    address = AddressModel.objects.all()
    return render(request,'pages/users/photo-gallery.html',{'gall':gall,'address':address,})


def membership(request):
    member = Membership.objects.all()
    benefit = Benefit.objects.all()
    address = AddressModel.objects.all()
    context={
        'member':member,
        'benefit':benefit,
        'address':address,
    }
    return render(request,'pages/users/membership.html',context)



def downloads(request):
    files = Downloads.objects.all()
    address = AddressModel.objects.all()
    return render(request,'pages/users/downloads.html',{'files':files,'address':address})



def projects(request):
    address = AddressModel.objects.all()
    partner = Partner.objects.all()
    return render(request,'pages/users/projects.html',{'partner':partner,'address':address})

##membership form###
def individual_form(request):
    address = AddressModel.objects.all()
    if request.method == 'POST':
        form = IndividualForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data submitted successfully')
        else:
            messages.info(request,'Something went wrong!')
        return redirect('individual_form')
    else:
        form = IndividualForm()
    
    return render(request,'pages/users/individual-form.html', {'form': form,'address':address,})



def organization_form(request):
    address = AddressModel.objects.all()
    if request.method == 'POST':
        form = OrganizationForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Data submitted successfully')
        else:
            messages.info(request,'Something went wrong!')
        return redirect('organization_form')
    else:
        form = OrganizationForm()
    
    return render(request,'pages/users/organization-form.html', {'form': form,'address':address,})

