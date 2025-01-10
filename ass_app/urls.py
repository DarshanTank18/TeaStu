from django.contrib import admin
from django.urls import path,include
from ass_app import views
from ass_project import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('sign_in/',views.sign_in, name="sign_in"),
    path('sign_up/',views.sign_up),
    path('staff/',views.staff),
    path('teachers/',views.teachers, name="teachers"),
    path('add_teacher/',views.add_teacher),
    path('loguot/',views.loguot),
    path('delete/<int:id>/',views.delete),
    path('student',views.student),
    path('add_student/',views.add_student),
    path('header/',views.header),
    path('Profile/',views.profile,name='Profile'),
    path('emailverify/',views.emailverify,name="emailverify"),
    path('delete_acc/<int:id>',views.delete_acc),
    path('event/',views.event),
    path('edit_user/',views.edit_user),
    path('change_pass/',views.change_pass, name='change_pass'),
    path('department/',views.department),
    path('campus/',views.campus),
    path('club/',views.club, name="club"),
    path('add_club/',views.add_club),
    path('library/',views.library, name="library"),
    path('add_book/',views.add_book),
    path('routine/',views.routine),
    # path('404',)
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)