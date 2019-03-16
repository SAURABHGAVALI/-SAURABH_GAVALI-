"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_view),
    url(r'^blog.html/', views.Blog_view),
    url(r'^service.html/', views.SERVICE_VIEW),
    url(r'^elements.html/', views.Elemente_VIEW),
    url(r'^About1.html/', views.ABOUT_VIEW),
    url(r'^spartan.html/', views.SPARTAN_VIEW),
    url( r'^food.html/', views.Food_VIEW),
    url( r'^Work-out.html/', views.Work_VIEW),
    url( r'^NUTRITION/', views.Diet_VIEW),
    url(r'^$', views.home_view),
    url(r'^BMI/', views.bmi_view),
    url(r'^logout123/', views.logout_view),
    url(r'^signup/', views.signup_view),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^blog/', views.post_list_view),
     # url(r'^$', views.PostListView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view,name='post_detail'),
    url(r'^(?P<id>\d+)/share/$',views.mail_send_view),
    url(r'^GymR/',views.Ginsert_view),
    url(r'^MeditationR/',views.Minsert_view),
    url(r'^YogaR/',views.Yinsert_view),
    url(r'^ADVENTURER/',views.ADinsert_view),
    url(r'^THANKS/',views.TM_VIEW),
    url(r'^BegineR/',views.GB_VIEW),
    url(r'^Moderate/',views.GM_VIEW),
    url(r'^Advanced/',views.GA_VIEW),
    url(r'^MEDITATION/',views.MD_VIEW),
    url(r'^AdventureWORLD/',views.AV_VIEW),
    url(r'^feedback/', views.feedback_form_view),
    url(r'^pranic/', views.PR_VIEW),
    url(r'^PRE/', views.PH_view),

]
