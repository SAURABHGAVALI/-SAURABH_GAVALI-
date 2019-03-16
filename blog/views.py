from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.forms import SignUpForm
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import RegistrationYForm
from blog.forms import ADVENTUREForm
from blog.forms import GYMForm
from blog.forms import MEDITATIONForm
from django.shortcuts import render,redirect

# Create your views here.
def home_view(request):
    return render(request,'testapp/Home.html')
@login_required
def java_exams_view(request):
    return render(request,'testapp/java.html')

def logout_view(request):
    return render(request,'testapp/login.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})

def index_view(request):
    return render(request,'testapp/index.html')

def Blog_view(request):
    return render(request,'testapp/blog.html')

def JOIN_US_VIEW(request):
    return render(request,'testapp/contact.html')

def SERVICE_VIEW(request):
    return render(request,'testapp/services.html')

def Elemente_VIEW(request):
    return render(request,'testapp/elements.html')


def MAIN_VIEW(request):
    return render(request,'testapp/MAIN.html')


def FITNEZZ_VIEW(request):
    return render(request,'testapp/FITNEZZ.html')

def ABOUT_VIEW(request):
    return render(request,'testapp/About1.html')

def SPARTAN_VIEW(request):
    return render(request,'testapp/spartan.html')

def Food_VIEW(request):
    return render(request,'testapp/food.html')

def Work_VIEW(request):
    return render(request,'testapp/Work-out.html')

def Diet_VIEW(request):
    return render(request,'testapp/DIET-PLAN.html')


def Ginsert_view(request):
    form=GYMForm()
    if request.method=='POST':
        form=GYMForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/THANKS')
    return render(request,'testapp1/insert.html',{'form':form})


def Minsert_view(request):
    form=MEDITATIONForm()
    if request.method=='POST':
        form=MEDITATIONForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/THANKS')
    return render(request,'testapp1/meditation.html',{'form':form})


def Yinsert_view(request):
    form=RegistrationYForm()
    if request.method=='POST':
        form=RegistrationYForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/THANKS')
    return render(request,'testapp1/yoga.html',{'form':form})

def ADinsert_view(request):
    form=ADVENTUREForm()
    if request.method=='POST':
        form=ADVENTUREForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/THANKS')
    return render(request,'testapp1/insert.html',{'form':form})

def  PH_view(request):
    form=ADVENTUREForm()
    if request.method=='POST':
        form=ADVENTUREForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/THANKS')
    return render(request,'testapp1/insert.html',{'form':form})


# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/post_list.html',{'post_list':post_list})

from django.views.generic import ListView
class PostListView(ListView):
    model=Post
    paginate_by=1

def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    return render(request,'blog/post_detail.html',{'post':post})

from django.core.mail import send_mail
from blog.forms import EmailSendForm

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recommends you to read"{}"'.format(cd['name'],cd['email'],post.title)
            post_url=request.build_absolute_uri(post.get_absolute_url())
            message='Read Post At:\n {}\n\n{}\'s Comments:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'gavalisaurabh90@gmail.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,'blog/sharebymail.html',{'form':form,'post':post,'sent':sent})


def GM_VIEW(request):
    return render(request,'GYM/Moderate.html')
def GA_VIEW(request):
    return render(request,'GYM/Advanced.html')

def GB_VIEW(request):
    return render(request,'GYM/BegineR.html')

def MD_VIEW(request):
    return render(request,'MEDITATION/MEDITATION1.html')
def AV_VIEW(request):
    return render(request,'Adventure/ADVENTURES.html')

def TM_VIEW(request):
    return render(request,'ThanksMain.html')

from blog.forms import FeedbackForm

# Create your views here.
def feedback_form_view(request):
    form=FeedbackForm()
    # feedback_submitted=False
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print('Basic Validation Completed and Printing Data')
            print('name:',form.cleaned_data['name'])
            print('age:',form.cleaned_data['age'])
            print('Email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])            # feedback_submitted=True
    return render(request,'feedback.html',{'form':form})

def PR_VIEW(request):
    return render (request,'pranich.html')


def Diet_VIEW(request):

    return render(request,'dietplan/AdvancedE.html')

def bmi_view(request):
     return render(request,'BMI.html')
