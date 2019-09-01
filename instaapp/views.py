


from django.http  import HttpResponse,Http404
from .models import Image,NewsLetterRecipients,Profile
from django.shortcuts import render,redirect
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import NewArticleForm, NewsLetterForm, NewsProfileForm



@login_required(login_url='/accounts/login/')
def home(request):
    current_user =request.user
    posts = Image.objects.all()
    profile = Profile.objects.get(username=current_user)
    users = Profile.objects.all()
    
    return render(request, 'home.html', {"posts":posts,"profile":profile, "users":users, })

# Create your views here.
def login_page(request):
    return render(request, 'registration/welcome.html')
@login_required(login_url='/accounts/login/')
def insta(request):
    
    insta = Image.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('insta')
    else:
        form = NewsLetterForm()
    return render(request, 'insta/main-posts.html', {"insta":insta,"letterForm":form})




def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewsProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.user_id=current_user.id
            profile.save()
        return redirect('user')
    else:
        form = NewsProfileForm()
    return render(request, 'profile.html', {"form":form})
@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('user')

    else:
        form = NewArticleForm()
    return render(request, 'new-article.html', {"form": form}) 
@login_required(login_url='/accounts/login/')
def user(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    posts=Image.objects.filter(profile_id=current_user.id)
    return render(request, 'user-post.html',{"profile":profile,"posts":posts})