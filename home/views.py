from django.shortcuts import render, get_object_or_404
from jinja2 import Environment, FileSystemLoader
from django.http import HttpResponse
from .models import Post







# Define jinja_render function
def jinja_render(template_name, context):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    rendered_template = template.render(context)
    return HttpResponse(rendered_template)

# Create your views here.
def show_post(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return jinja_render('home.jinja', context)




def show_detail_post(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return jinja_render('details.jinja', context)

