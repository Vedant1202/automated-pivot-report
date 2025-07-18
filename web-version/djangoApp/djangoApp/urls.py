"""
URL configuration for djangoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from djangoWebApp.views import protected_page, get_recruitment_data_from_mongo, get_mdreview_data_from_mongo, get_available_dates
from djangoWebApp.views import (
    fetch_and_store_data_for_ignite, get_saved_data_for_ignite, ignite_report_page, aced_report_page, get_detailed_staff_report, get_selfharm_summary, get_ignite_intervention_report,
    get_aced_recruitment_data, get_aced_exclusions_refusals_data
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('protected/', protected_page, name='protected_page'),
    path('api/data/recruitment/', get_recruitment_data_from_mongo, name='get_recruitment_data_from_mongo'),
    path('api/data/mdreview/', get_mdreview_data_from_mongo, name='get_mdreview_data_from_mongo'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('api/dates/', get_available_dates, name='get_available_dates'),
    # 🔥 New Ignite Recruitment Routes 🔥
    path('ignite/fetch/', fetch_and_store_data_for_ignite, name='fetch_data_for_ignite'),
    path('ignite/data/', get_saved_data_for_ignite, name='get_saved_data_for_ignite'),
    path('ignite/report/', ignite_report_page, name='ignite_report'),
    path('ignite/detailed-staff-report/', get_detailed_staff_report, name='get_detailed_staff_report'),
    path('ignite/self-harm-report/', get_selfharm_summary, name='self-harm-report'),
    path('ignite/intervention/', get_ignite_intervention_report, name='ignite_intervention_report'),

    # ACED Routes
    path('aced/report/', aced_report_page, name='aced_report'),
    path('aced/recruitment/', get_aced_recruitment_data, name='aced_recruitment_report'),
    path('aced/exclusions-refusals/', get_aced_exclusions_refusals_data, name='get_aced_exclusions_refusals_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

from django.conf.urls import handler404
from djangoWebApp.views import custom_404_view

handler404 = custom_404_view
