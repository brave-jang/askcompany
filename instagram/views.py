from django.db import models
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'post_list':qs,
        'q' : q,
    })


# def post_detail(request, pk):
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "instagram/post_detail.html", {
#         'post':post
#     })

post_detail = DetailView.as_view(model=Post)