"""YountanYargyas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about/", views.aboutpage, name="aboutpage"),
    path("contact/", views.contactpage, name="contactpage"),
    path("help/", views.helppage, name="helppage"),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login_request"),
    path("change-password/", views.change_password, name="change_password"),
    path("logout/", views.logout_request, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("upload/", views.upload, name="upload"),
    path("upload/images", views.upload_images, name="upload_images"),
    path("upload/videos", views.upload_videos, name="upload_videos"),
    path("upload/audios", views.upload_audios, name="upload_audios"),
    path("upload/files", views.upload_files, name="upload_files"),
    path("student-feed/", views.student_feed, name="student_feed"),
    path("student-feed/feed", views.sf_feed, name="sf_feed"),
    path("student-feed/profiles", views.sf_profiles, name="sf_profiles"),
    path("student-feed/profiles/<slug:username_slug>", views.sf_profile_posts, name="sf_profile_posts"),
    path("student-feed/posts", views.sf_posts, name="sf_posts"),
    path("messages/", views.messages_section, name="messages_section"),
    path("messages/<slug:username_slug>", views.messages_chat, name="messages_chat"),
    path("classes/", views.student_classes, name="student_classes"),
    path("classes/<slug:class_slug>", views.student_class, name="student_class"),
    path("classes/<slug:class_slug>/<slug:subject_slug>", views.student_subject, name="student_subject"),
    path("classes/<slug:class_slug>/<slug:subject_slug>/<slug:chapter_slug>", views.student_chapter, name="student_chapter"),
    path("classes/<slug:class_slug>/<slug:subject_slug>/<slug:chapter_slug>/<slug:section_slug>", views.student_section, name="student_section"),
    path("delete-data", views.delete_data, name="delete_data"),
    path("edit-data", views.edit_data, name="edit_data"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
