from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, ResumeItem, Testimonial, Skill
from django.views.generic import DetailView

def home(request):
    context = {
        'posts': Post.objects.all(),
        'resume_items': ResumeItem.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'skills': Skill.objects.all()
    }
    return render(request, 'blog/index.html', context)

class SinglePostView(DetailView):
    model = Post