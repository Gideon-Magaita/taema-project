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
    }
    return render(request, 'pages/users/home.html', context)



def main_view(request):
    contact_info = AddressModel.objects.all()
    return render(request, 'pages/users/main.html', {'contact_info': contact_info})



def news(request):
    news_list = News.objects.all().order_by('-date')  # Order by latest news first
    paginator = Paginator(news_list, 6)  # Show 6 news items per page

    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)

    context = {
        'news': news_page,
    }
    return render(request, 'pages/users/news.html', context)



def news_details(request,id):
    news = News.objects.get(id=id)
    return render(request,'pages/users/news-details.html',{'news':news})



def about(request):
    who = WhoAreWe.objects.all()
    content = Mission.objects.all()
    vision = Vision.objects.all()
    objective = Objective.objects.all()
    context={
        'who':who,
        'content':content,
        'vision':vision,
        'objective':objective
    }
    return render(request,'pages/users/about.html',context)


def contact(request):
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
        'address':address
    }
    return render(request,'pages/users/contact.html',context)




def works(request):
    return render(request,'pages/users/works.html')



def working_groups(request):
    work = WorkingGroup.objects.all()
    return render(request,'pages/users/working-group.html',{'work':work})


def photo_gall(request):
    gall = Gallery.objects.all()
    return render(request,'pages/users/photo-gallery.html',{'gall':gall})


def membership(request):
    member = Membership.objects.all()
    benefit = Benefit.objects.all()
    context={
        'member':member,
        'benefit':benefit,
    }
    return render(request,'pages/users/membership.html',context)



def downloads(request):
    files = Downloads.objects.all()
    return render(request,'pages/users/downloads.html',{'files':files})



def projects(request):
    partner = Partner.objects.all()
    return render(request,'pages/users/projects.html',{'partner':partner})