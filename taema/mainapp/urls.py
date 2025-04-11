from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static 
from .import admins

urlpatterns=[
    path('',views.home,name='home'),
    path('main_view',views.main_view,name='main_view'),
    path('news',views.news,name='news'),
    path('news_details/<int:id>',views.news_details,name='news_details'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('works',views.works,name='works'),
    path('membership',views.membership,name='membership'),
    path('downloads',views.downloads,name='downloads'),
    path('projects',views.projects,name='projects'),
    path('working_groups',views.working_groups,name='working_groups'),
    path('photo_gall',views.photo_gall,name='photo_gall'),
    #authenticationurls
    path('login_user', admins.login_user,name='login_user'),
    path('logoutUser', admins.logoutUser,name='logoutUser'),

    #adminurls
    path('admin_home',admins.admin_home,name='admin_home'),
    #sliders
    path('sliders',admins.sliders,name='sliders'),
    path('edit_sliders/<int:id>',admins.edit_sliders,name='edit_sliders'),
    path('delete_sliders/<int:id>',admins.delete_sliders,name='delete_sliders'),
    #welcome note
    path('welcome_note',admins.welcome_note,name='welcome_note'),
    path('edit_welcome_note/<int:id>',admins.edit_welcome_note,name='edit_welcome_note'),
    path('delete_welcome_note/<int:id>',admins.delete_welcome_note,name='delete_welcome_note'),
    #activity urls
    path('activity_performed',admins.activity_performed,name='activity_performed'),
    path('edit_activity_performed/<int:id>',admins.edit_activity_performed,name='edit_activity_performed'),
    path('delete_activity_performed/<int:id>',admins.delete_activity_performed,name='delete_activity_performed'),
    #board member
    path('board_member',admins.board_member,name='board_member'),
    path('edit_board_member/<int:id>',admins.edit_board_member,name='edit_board_member'),
    path('delete_board_member/<int:id>',admins.delete_board_member,name='delete_board_member'),
    #comment url
    path('comment_function',admins.comment_function,name='comment_function'),
    path('edit_comment_function/<int:id>',admins.edit_comment_function,name='edit_comment_function'),
    path('delete_comment_function/<int:id>',admins.delete_comment_function,name='delete_comment_function'),
    #Who are we urls
    path('who_are_we',admins.who_are_we,name='who_are_we'),
    path('edit_who_are_we/<int:id>',admins.edit_who_are_we,name='edit_who_are_we'),
    path('delete_who_are_we/<int:id>',admins.delete_who_are_we,name='delete_who_are_we'),
    #mission
    path('mission_function',admins.mission_function,name='mission_function'),
    path('edit_mission/<int:id>',admins.edit_mission,name='edit_mission'),
    path('delete_mission/<int:id>',admins.delete_mission,name='delete_mission'),
    #vision
    path('vision_function',admins.vision_function,name='vision_function'),
    path('edit_vision/<int:id>',admins.edit_vision,name='edit_vision'),
    path('delete_vision/<int:id>',admins.delete_vision,name='delete_vision'),
    #objectives
    path('objective_function',admins.objective_function,name='objective_function'),
    path('edit_objective/<int:id>',admins.edit_objective,name='edit_objective'),
    path('delete_objective/<int:id>',admins.delete_objective,name='delete_objective'),
    #news
    path('news_update',admins.news_update,name='news_update'),
    path('edit_news_update/<int:id>',admins.edit_news_update,name='edit_news_update'),
    path('delete_news_update/<int:id>',admins.delete_news_update,name='delete_news_update'),
    #memberurls
    path('member_function',admins.member_function,name='member_function'),
    path('edit_member/<int:id>',admins.edit_member,name='edit_member'),
    path('delete_member/<int:id>',admins.delete_member,name='delete_member'),
    #benefitsurls
    path('member_benefits',admins.member_benefits,name='member_benefits'),
    path('edit_member_benefits/<int:id>',admins.edit_member_benefits,name='edit_member_benefits'),
    path('delete_member_benefits/<int:id>',admins.delete_member_benefits,name='delete_member_benefits'),
    #working group
    path('working_group',admins.working_group,name='working_group'),
    path('edit_working_group/<int:id>',admins.edit_working_group,name='edit_working_group'),
    path('delete_working_group/<int:id>',admins.delete_working_group,name='delete_working_group'),
    #Gallery
    path('photo_gallery',admins.photo_gallery,name='photo_gallery'),
    path('edit_photo_gallery/<int:id>',admins.edit_photo_gallery,name='edit_photo_gallery'),
    path('delete_photo_gallery/<int:id>',admins.delete_photo_gallery,name='delete_photo_gallery'),
    #contacturls
    path('admin_contact',admins.admin_contact,name='admin_contact'),
    path('delete_contact/<int:id>',admins.delete_contact,name='delete_contact'),
    #partner&projecturl
    path('project_partner',admins.project_partner,name='project_partner'),
    path('edit_project_partner/<int:id>',admins.edit_project_partner,name='edit_project_partner'),
    path('delte_project_partner/<int:id>',admins.delte_project_partner,name='delte_project_partner'),
    #addressurls
    path('address_path',admins.address_path,name='address_path'),
    path('edit_address_path/<int:id>',admins.edit_address_path,name='edit_address_path'),
    path('delete_address_path/<int:id>',admins.delete_address_path,name='delete_address_path'),
    #other links urls
    path('file_downloads',admins.file_downloads,name='file_downloads'),
    path('delete_file_download/<int:id>',admins.delete_file_download,name='delete_file_download'),
    path('edit_file_download/<int:id>',admins.edit_file_download,name='edit_file_download'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)