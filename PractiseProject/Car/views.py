from django.shortcuts import render,redirect
from . import forms 
from . import models
from django.contrib import messages
from django.contrib.auth import logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
# Create your views here.

class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    



def signUp(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Accaunt Created Successfully')
            return redirect('login')
    else:
        form = forms.SignUpForm()
    return render(request,'Car/SignUp.html',{'form':form,'type':'SignUp'})

class UserLoginView(LoginView):
    template_name= 'Car/SignUp.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self,form):
        messages.success(self.request,'Logged in Successfully')
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.warning(self.request,'Logged in information incerrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@login_required
def profile(request):
    return render(request,'Car/profile.html')

def editProfile(request):
    if request.method == 'POST':
        form = forms.ChangeUserForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile')
    else:
        form = forms.ChangeUserForm(instance = request.user)
    return render(request,'Car/update_profile.html',{'form':form})

@login_required
def user_logout(request):
    logout(request)
    messages.warning(request,'Logged Out Successfull')
    return redirect('login')

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Password Updated Successfuly")
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'Car/pass_change.html',{'form':form})


class DetailsPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'Car/post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

