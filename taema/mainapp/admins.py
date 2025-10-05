from email import message
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
#counting visitors imports
from django.utils.timezone import now
from datetime import timedelta
#authentication
from django.contrib.auth.models import Group
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
#change password
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChangeCustomForm
from django.urls import reverse_lazy



#authentication functions
@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_home')
        else:
            messages.info(request,'username or password is incorrect') 

    return render(request,'pages/auth/login.html')




def logoutUser(request):
    logout(request)
    return redirect('login_user')

#change password class
class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeCustomForm
    template_name = 'pages/admins/change-password.html'
    success_url = reverse_lazy('password_change_done')


@login_required(login_url='login_user')
@admin_only
def admin_home(request):
    """View for the admin dashboard showing visitor statistics."""
    today = now().date()
    week_start = today - timedelta(days=today.weekday())  # Start of the current week
    month_start = today.replace(day=1)  # Start of the current month

    # Count visitors
    total_visitors = Visitor.objects.count()
    daily_visitors = Visitor.objects.filter(visit_time__date=today).count()
    weekly_visitors = Visitor.objects.filter(visit_time__date__gte=week_start).count()
    monthly_visitors = Visitor.objects.filter(visit_time__date__gte=month_start).count()

    context = {
        'total_visitors': total_visitors,
        'daily_visitors': daily_visitors,
        'weekly_visitors': weekly_visitors,
        'monthly_visitors': monthly_visitors,
    }
    
    return render(request, 'pages/admins/home.html', context)



@login_required(login_url='login_user')
@admin_only
def sliders(request):
    slider = Slider.objects.all()
    if request.method == 'POST':
        form = SliderForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Slider saved successfully')
        else:
            messages.error(request,'Sothing went wrong')
        return redirect('sliders')
    else:
        form = SliderForm()
    context={
        'form':form,
        'slider':slider,
    }
    return render(request,'pages/admins/sliders.html',context)


@login_required(login_url='login_user')
@admin_only
def edit_sliders(request,id):
    slide = Slider.objects.get(id=id)
    if request.method == 'POST':
        form = SliderForm(request.POST or None,request.FILES or None,instance=slide)
        if form.is_valid():
            form.save()
            messages.success(request,'Slider updated successfully!')
        else:
            messages.error(request,'Something went wrong! Please try again')
        return redirect('sliders')
    else:
        form = SliderForm(instance=slide)
    context={
        'form':form,
    }
    return render(request,'pages/admins/edit-slider.html',context)


@login_required(login_url='login_user')
@admin_only
def delete_sliders(request,id):
    slide = Slider.objects.get(id=id)
    slide.delete()
    if slide:
        messages.success(request,'Slider deleted successfully!')
    else:
        messages.error(request,'Something went wrong! Please try again')
    return redirect('sliders')

#welcome note function

@login_required(login_url='login_user')
@admin_only
def welcome_note(request):
    welcome = WelcomeNote.objects.all()
    if request.method == 'POST':
        form = WelcomeNoteForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Welcome note saved successfully')
        else:
            messages.error(request,'Something went wrong! Please try again')
        return redirect('welcome_note')
    else:
        form = WelcomeNoteForm()
    context={
        'form':form,
        'welcome':welcome,
    }
    return render(request,'pages/admins/welcome.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_welcome_note(request,id):
    welcome = WelcomeNote.objects.get(id=id)
    if request.method == 'POST':
        form = WelcomeNoteForm(request.POST or None,request.FILES or None,instance=welcome)
        if form.is_valid():
            form.save()
            messages.success(request,'Welcome note updated!')
        else:
            messages.error(request,'Something went wrong')
        return redirect('welcome_note')
    else:
        form = WelcomeNoteForm(instance=welcome)
    context={
        'form': form,
    }
    return render(request,'pages/admins/edit-welcome.html', context)



@login_required(login_url='login_user')
@admin_only
def delete_welcome_note(request,id):
    welcome = WelcomeNote.objects.get(id=id)
    welcome.delete()
    if welcome:
        messages.success(request,'Welcome Note deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('welcome_note')
#welcome note function ends here



#activity function
@login_required(login_url='login_user')
@admin_only
def activity_performed(request):
    activity = Activity.objects.all()
    if request.method == 'POST':
        form = ActivityForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Activity saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('activity_performed')
    else:
        form = ActivityForm()
    context={
        'form':form,
        'activity':activity,
    }
    return render(request,'pages/admins/activity.html', context)



@login_required(login_url='login_user')
@admin_only
def edit_activity_performed(request,id):
    activity = Activity.objects.get(id=id)
    if request.method == 'POST':
        form = ActivityForm(request.POST or None,instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request,'Activity updated successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('activity_performed')
    else:
        form = ActivityForm(instance=activity)
    context={
        'form':form,
    }
    return render(request,'pages/admins/edit-activity.html', context)


@login_required(login_url='login_user')
@admin_only
def delete_activity_performed(request,id):
    activity = WelcomeNote.objects.get(id=id)
    activity.delete()
    if activity:
        messages.success(request,'Welcome Note deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('welcome_note')
#Ends activity function


#Board member function
@login_required(login_url='login_user')
@admin_only
def board_member(request):
    member = BoardMember.objects.all()
    if request.method == 'POST':
        form = BoardMemberForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Members saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('board_member')
    else:
        form = BoardMemberForm()
    context={
        'form': form,
        'member':member,
    }
    return render(request,'pages/admins/board-member.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_board_member(request,id):
    member = BoardMember.objects.get(id=id)
    if request.method == 'POST':
        form = BoardMemberForm(request.POST or None,instance=member)
        if form.is_valid():
            form.save()
            messages.success(request,'Members updated successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('board_member')
    else:
        form =  BoardMemberForm(instance=member)
    context={
        'form':form,
    }
    return render(request,'pages/admins/edit-board-member.html', context)



@login_required(login_url='login_user')
@admin_only
def delete_board_member(request,id):
    member = BoardMember.objects.get(id=id)
    member.delete()
    if member:
        messages.success(request,'Member deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('board_member')
#Board member function ends here



#Comment functions
@login_required(login_url='login_user')
@admin_only
def comment_function(request):
    comment = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Comments saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('comment_function')
    else:
        form = CommentForm()
    context={
        'form': form,
        'comment':comment,
    }
    return render(request,'pages/admins/comments.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_comment_function(request,id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST or None,instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request,'Comment updated successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('comment_function')
    else:
        form =  CommentForm(instance=comment)
    context={
        'form':form,
    }
    return render(request,'pages/admins/edit-comment.html', context)


@login_required(login_url='login_user')
@admin_only
def delete_comment_function(request,id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    if comment:
        messages.success(request,'Comment deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('comment_function')
#Comment functions ends here


#Who are we functions
@login_required(login_url='login_user')
@admin_only
def who_are_we(request):
    content = WhoAreWe.objects.all()
    if request.method == 'POST':
        form = WhoAreWeForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Content saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('who_are_we')
    else:
        form = WhoAreWeForm()
    context={
        'form': form,
        'content':content,
    }
    return render(request,'pages/admins/who.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_who_are_we(request,id):
    content = WhoAreWe.objects.get(id=id)
    if request.method == 'POST':
        form = WhoAreWeForm(request.POST or None,request.FILES or None,instance=content)
        if form.is_valid():
            form.save()
            messages.success(request,'Content saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('who_are_we')
    else:
        form = WhoAreWeForm(instance=content)
    context={
        'form': form,
    }
    return render(request,'pages/admins/edit-who.html',context)


@login_required(login_url='login_user')
@admin_only
def delete_who_are_we(request,id):
    content = WhoAreWe.objects.get(id=id)
    content.delete()
    if content:
        messages.success(request,'Content deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('who_are_we')



#mission function
@login_required(login_url='login_user')
@admin_only
def mission_function(request):
    content = Mission.objects.all()
    if request.method == 'POST':
        form = MissionForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Mission saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('mission_function')
    else:
        form = MissionForm()
    context={
        'form': form,
        'content':content,
    }
    return render(request,'pages/admins/mission.html',context)




@login_required(login_url='login_user')
@admin_only
def edit_mission(request,id):
    content = Mission.objects.get(id=id)
    if request.method == 'POST':
        form = MissionForm(request.POST or None,request.FILES or None,instance=content)
        if form.is_valid():
            form.save()
            messages.success(request,'Mission saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('mission_function')
    else:
        form = MissionForm(instance=content)
    context={
        'form': form,
    }
    return render(request,'pages/admins/edit-mission.html',context)




@login_required(login_url='login_user')
@admin_only
def delete_mission(request,id):
    content = Mission.objects.get(id=id)
    content.delete()
    if content:
        messages.success(request,'Mission deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('mission_function')
#mission function ends here


#vision
@login_required(login_url='login_user')
@admin_only
def vision_function(request):
    content = Vision.objects.all()
    if request.method == 'POST':
        form = VisionForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Vision saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('vision_function')
    else:
        form = VisionForm()
    context={
        'form': form,
        'content':content,
    }
    return render(request,'pages/admins/vision.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_vision(request,id):
    content = Vision.objects.get(id=id)
    if request.method == 'POST':
        form = VisionForm(request.POST or None,request.FILES or None,instance=content)
        if form.is_valid():
            form.save()
            messages.success(request,'Vision saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('vision_function')
    else:
        form = VisionForm(instance=content)
    context={
        'form': form,
    }
    return render(request,'pages/admins/edit-vision.html',context)


@login_required(login_url='login_user')
@admin_only
def delete_vision(request,id):
    content = Vision.objects.get(id=id)
    content.delete()
    if content:
        messages.success(request,'Vision deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('vision_function')

#endvisionfunction

#objective
@login_required(login_url='login_user')
@admin_only
def objective_function(request):
    content = Objective.objects.all()
    if request.method == 'POST':
        form = ObjectiveForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Objective saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('objective_function')
    else:
        form = ObjectiveForm()
    context={
        'form': form,
        'content':content,
    }
    return render(request,'pages/admins/objectives.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_objective(request,id):
    content = Objective.objects.get(id=id)
    if request.method == 'POST':
        form = ObjectiveForm(request.POST or None,request.FILES or None,instance=content)
        if form.is_valid():
            form.save()
            messages.success(request,'Objective saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('objective_function')
    else:
        form = ObjectiveForm(instance=content)
    context={
        'form': form,
    }
    return render(request,'pages/admins/edit-objectives.html',context)



@login_required(login_url='login_user')
@admin_only
def delete_objective(request,id):
    content = Objective.objects.get(id=id)
    content.delete()
    if content:
        messages.success(request,'Objective deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('objective_function')
#endobjectivefunction


#News and Updates
@login_required(login_url='login_user')
@admin_only
def news_update(request):
    news = News.objects.all()
    if request.method == 'POST':
        form = NewsForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'News saved successfully')
        else:
            messages.error(request,'Sothing went wrong')
        return redirect('news_update')
    else:
        form = NewsForm()
    context={
        'form':form,
        'news':news,
    }
    return render(request,'pages/admins/news.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_news_update(request,id):
    news = News.objects.get(id=id)
    if request.method == 'POST':
        form = NewsForm(request.POST or None,request.FILES or None,instance=news)
        if form.is_valid():
            form.save()
            messages.success(request,'News updated successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('news_update')
    else:
        form = NewsForm(instance=news)
    context={
        'form': form,
    }
    return render(request,'pages/admins/edit-news.html',context)



@login_required(login_url='login_user')
@admin_only
def delete_news_update(request,id):
    news = News.objects.get(id=id)
    news.delete()
    if news:
        messages.success(request,'News deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('news_update')


@login_required(login_url='login_user')
@admin_only
def member_function(request):
    member = Membership.objects.all()
    if request.method == 'POST':
        form = MembershipForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Membership saved successfully')
        else:
            messages.error(request,'Sothing went wrong')
        return redirect('member_function')
    else:
        form = MembershipForm()
    context={
        'form':form,
        'member':member,
    }
    return render(request,'pages/admins/membership.html',context)


@login_required(login_url='login_user')
@admin_only
def edit_member(request,id):
    member = Membership.objects.get(id=id)
    if request.method == 'POST':
        form = MembershipForm(request.POST or None,instance=member)
        if form.is_valid():
            form.save()
            messages.success(request,'Membership updated successfully')
        else:
            messages.error(request,'Sothing went wrong')
        return redirect('member_function')
    else:
        form = MembershipForm(instance=member)
    context={
        'form':form,
    }
    return render(request,'pages/admins/edit-membership.html',context)



@login_required(login_url='login_user')
@admin_only
def delete_member(request,id):
    member = Membership.objects.get(id=id)
    member.delete()
    if member:
        messages.success(request,'Member deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('member_function')



@login_required(login_url='login_user')
@admin_only
def member_benefits(request):
    benefit = Benefit.objects.all()
    if request.method == 'POST':
        form = BenefitForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Benefit saved successfully')
        else:
            messages.error(request,'Sothing went wrong')
        return redirect('member_benefits')
    else:
        form = BenefitForm()
    context={
        'form':form,
        'benefit':benefit,
    }
    return render(request,'pages/admins/benefits.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_member_benefits(request,id):
    benefit = Benefit.objects.get(id=id)
    if request.method == 'POST':
        form = BenefitForm(request.POST or None,request.FILES or None,instance=benefit)
        if form.is_valid():
            form.save()
            messages.success(request,'Benefit updated successfully')
        else:
            messages.error(request,'Sothing went wrong')
        return redirect('member_benefits')
    else:
        form = BenefitForm(instance=benefit)
    context={
        'form':form,
    }
    return render(request,'pages/admins/edit-benefits.html',context)


@login_required(login_url='login_user')
@admin_only
def delete_member_benefits(request,id):
    benefit = Benefit.objects.get(id=id)
    benefit.delete()
    if benefit:
        messages.success(request,'Benefit deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('member_benefits')


#Working group functions######
@login_required(login_url='login_user')
@admin_only
def working_group(request):
    group = WorkingGroup.objects.all()
    if request.method == 'POST':
        form = WorkingGroupForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Contents saved successfully')
        else:
            messages.error(request,'Sothing went wrong')
        return redirect('working_group')
    else:
        form = WorkingGroupForm()
    context={
        'form':form,
        'group':group,
    }
    return render(request,'pages/admins/working-groups.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_working_group(request,id):
    group = WorkingGroup.objects.get(id=id)
    if request.method == 'POST':
        form = WorkingGroupForm(request.POST or None,instance=group)
        if form.is_valid():
            form.save()
            messages.success(request,'Content updated successfully')
        else:
            messages.error(request,'Sothing went wrong')
        return redirect('working_group')
    else:
        form = WorkingGroupForm(instance=group)
    context={
        'form':form,
        'group':group,
    }
    return render(request,'pages/admins/edit-working-groups.html',context)


@login_required(login_url='login_user')
@admin_only
def delete_working_group(request,id):
    group = WorkingGroup.objects.get(id=id)
    group.delete()
    if group:
        messages.success(request,'Working group deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('working_group')


#####Photo Gallery######
@login_required(login_url='login_user')
@admin_only
def photo_gallery(request):
    gall = Gallery.objects.all()
    if request.method == 'POST':
        form = GalleryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Photo gallery saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('photo_gallery')
    else:
        form = GalleryForm()
    context={
        'form': form,
        'gall':gall,
    }
    return render(request,'pages/admins/gallery.html',context)


@login_required(login_url='login_user')
@admin_only
def edit_photo_gallery(request,id):
    gall = Gallery.objects.get(id=id)
    if request.method == 'POST':
        form = GalleryForm(request.POST or None,request.FILES or None,instance=gall)
        if form.is_valid():
            form.save()
            messages.success(request,'Photo gallery updated successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('photo_gallery')
    else:
        form = GalleryForm(instance=gall)
    context={
        'form': form,
    }
    return render(request,'pages/admins/edit-gallery.html',context)


@login_required(login_url='login_user')
@admin_only
def delete_photo_gallery(request,id):
    gall = Gallery.objects.get(id=id)
    gall.delete()
    if gall:
        messages.success(request,'Gallery deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('photo_gallery')


@login_required(login_url='login_user')
@admin_only
def admin_contact(request):
    contact = Contact.objects.all()
    context={
        'contact':contact,
    }
    return render(request,'pages/admins/contact.html',context)



@login_required(login_url='login_user')
@admin_only
def delete_contact(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    if contact:
        messages.success(request,'Contact deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('admin_contact')



@login_required(login_url='login_user')
@admin_only
def project_partner(request):
    partner = Partner.objects.all()
    if request.method == 'POST':
        form = PartnerForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Content saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('project_partner')
    else:
        form = PartnerForm()
    context={
        'form': form,
        'partner':partner,
    }
    return render(request,'pages/admins/partner.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_project_partner(request,id):
    partner = Partner.objects.get(id=id)
    if request.method == 'POST':
        form = PartnerForm(request.POST or None,request.FILES or None,instance=partner)
        if form.is_valid():
            form.save()
            messages.success(request,'Content updated successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('project_partner')
    else:
        form = PartnerForm(instance=partner)
    context={
        'form': form,
    }
    return render(request,'pages/admins/edit-partner.html',context)



@login_required(login_url='login_user')
@admin_only
def delte_project_partner(request,id):
    partner = Partner.objects.get(id=id)
    partner.delete()
    if partner:
        messages.success(request,'Partner deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('project_partner')



@login_required(login_url='login_user')
@admin_only
def address_path(request):
    address = AddressModel.objects.all()
    if request.method == 'POST':
        form = AddressModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Contact saved successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('address_path')
    else:
        form = AddressModelForm()
    context={
        'form':form,
        'address':address,
    }
    return render(request,'pages/admins/address.html',context)



@login_required(login_url='login_user')
@admin_only
def edit_address_path(request,id):
    address = AddressModel.objects.get(id=id)
    if request.method == 'POST':
        form = AddressModelForm(request.POST or None,instance=address)
        if form.is_valid():
            form.save()
            messages.success(request,'Content updated successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('address_path')
    else:
        form = AddressModelForm(instance=address)
    context={
        'form': form,
    }
    return render(request,'pages/admins/edit-address.html',context)



@login_required(login_url='login_user')
@admin_only
def delete_address_path(request,id):
    address = AddressModel.objects.get(id=id)
    address.delete()
    if address:
        messages.success(request,'Content deleted successfully')
    else:
        messages.error(request,'Something went wrong')
    return redirect('address_path')


def file_downloads(request):
    files = Downloads.objects.all()
    if request.method == 'POST':
        form = DownloadsModelForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'File name saves successfully')
        else:
            messages.error(request,'Something went wrong!')
        return redirect('file_downloads')
    else:
        form = DownloadsModelForm()
    context={
        'form':form,
        'files':files,
    }
    return render(request,'pages/admins/downloads.html',context)



def edit_file_download(request,id):
    files = Downloads.objects.get(id=id)
    if request.method == 'POST':
        form = DownloadsModelForm(request.POST or None,request.FILES or None,instance=files)
        if form.is_valid():
            form.save()
            messages.success(request,'File name edited successfully')
        else:
            messages.error(request,'Something went wrong!')
        return redirect('file_downloads')
    else:
        form = DownloadsModelForm(instance=files)
    context={
        'form':form,
    }
    return render(request,'pages/admins/edit_download.html',context)



def delete_file_download(request,id):
    files = Downloads.objects.get(id=id)
    files.delete()
    if files:
        messages.success(request,'File deleted successfully')
    else:
        messages.error(request,'File deleted!')
    return redirect('file_downloads')


def specialization_area(request):
    if request.method=='POST':
        form = SpecializationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Data added successfuly!')
        else:
            messages.error(request,'Someting went wrong!')
        return redirect('specialization_area')
    else:
        form = SpecializationForm()
    spec = Specialization.objects.all()
    context={
        'form':form,
        'spec':spec,
    }
    return render(request,'pages/admins/specialization.html',context)


def edit_specialization_area(request,id):
    spec = Specialization.objects.get(id=id)
    if request.method=='POST':
        form = SpecializationForm(request.POST or None,instance=spec)
        if form.is_valid():
            form.save()
            messages.success(request,'Data updated successfuly!')
        else:
            messages.error(request,'Someting went wrong!')
        return redirect('specialization_area')
    else:
        form = SpecializationForm(instance=spec)
    context={
        'form':form,
    }
    return render(request,'pages/admins/edit-specialization.html',context)



def delete_specialization_area(request,id):
    files = Specialization.objects.get(id=id)
    files.delete()
    if files:
        messages.success(request,'Data deleted successfully')
    else:
        messages.error(request,'Data deleted!')
    return redirect('specialization_area')


def Individual_membership(request):
    indi = Individual.objects.all()
    return render(request,'pages/admins/individual-form.html',{'individuals':indi})


def organization_membership(request):
    organizations = Organization.objects.all()
    return render(request, 'pages/admins/organization-form.html', {'organizations': organizations})


@login_required(login_url='login_user')
@admin_only
def team_members(request):
    team = TeamMember.objects.all().order_by('-date_added')
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team member added successfully!')
            return redirect('team_members')
        else:
            messages.error(request, 'Something went wrong. Please check the form.')
    else:
        form = TeamMemberForm()
    context = {
        'form': form,
        'team': team,
    }
    return render(request, 'pages/admins/team.html', context)



@login_required(login_url='login_user')
@admin_only
def edit_team_member(request, id):
    member = get_object_or_404(TeamMember, id=id)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team member updated successfully!')
            return redirect('team_members')
        else:
            messages.error(request, 'Something went wrong.')
    else:
        form = TeamMemberForm(instance=member)
    context = {
        'form': form,
        'member': member,
    }
    return render(request, 'pages/admins/edit-team.html', context)


@login_required(login_url='login_user')
@admin_only
def delete_team_member(request, id):
    member = get_object_or_404(TeamMember, id=id)
    member.delete()
    messages.success(request, 'Team member deleted successfully!')
    return redirect('team_members')
