from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View

from .models import *
from .forms import CommentsForms, ContactForm

# Create your views here.
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'home.html')


class PostView(ListView):
    model = blog
    template_name = 'post.html'
    paginate_by = 3
    ordering = '-created_on'


class PostDetails(DetailView):
    model = blog
    template_name = 'post_details.html'


def about(request):
    return render(request, 'about.html')


class Contact(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'contact.html')

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            form.save()
            messages.info(self.request, "Thank for messaging us")
            return redirect('contact')
        else:
            messages.info(self.request, "You didn't complete the form")
            return redirect('contact')


def post_comment(request, pk=None):
    post_id = get_object_or_404(blog, pk=pk)
    if request.method == 'POST':
        form = CommentsForms(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            new_comment = comment()
            new_comment.content = content
            new_comment.author = request.user or None
            new_comment.create_on = timezone.now()
            new_comment.post = post_id
            new_comment.save()
            messages.success(request, 'thanks for adding your comment.Welcome again')
            return redirect('post_details', pk=post_id.pk)
        messages.success(request, 'Form not valid')
        return redirect('post_details', pk=post_id.pk)

    return redirect('post_details', pk=post_id.pk)
