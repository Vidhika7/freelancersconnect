"""
URL configuration for FreelancersConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from services import views as servicesViews
from accounts import views as accountsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', servicesViews.index, name='index'),
    path('post-project/', servicesViews.post_project, name='post_project'),
    path('post-a-job/',servicesViews.post_job,name='post-a-job'),
    path('about-us/', servicesViews.about_us, name='about_us'),
    path('profile/<int:user_id>/', servicesViews.freelancers_profile, name='freelancers_profile'),
    path('client/<int:user_id>/', servicesViews.client_profile, name='client_profile'),
     path('find-projects/', servicesViews.find_projects, name='find_projects'),
    path('project/<int:project_id>/', servicesViews.project_detail, name='project_detail'),
    path('project/<int:project_id>/send-proposal/', servicesViews.send_proposal, name='send_proposal'),
 
    path('search-freelancers/', accountsViews.search_freelancers, name='search_freelancers'),
    
    
    path('signup/', accountsViews.signup, name='signup'),
    path('signin/', accountsViews.signin, name='signin'),
    path('signout/', accountsViews.signout, name='signout'),
    path('forgot-password/', accountsViews.forgot_password, name='forgot_password'),
    path('verify-otp/',accountsViews.verifyOtp,name='verify_otp'),
    path('reset-password/<int:user_id>',accountsViews.resetPassword,name="reset_password"),
    path('edit-profile/', accountsViews.edit_profile, name='edit_profile'),
    path('delete-profile/', accountsViews.delete_profile, name='delete_profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)