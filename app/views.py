from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from app.forms import PostForm
from app.models import Post


# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(
        request,
        "app/index.html",
        {"post_list": qs},
    )


def post_detail(reqeust: HttpRequest, pk: int) -> HttpResponse:
    # qs = Post.objects.get(pk=pk)
    qs = get_object_or_404(Post, pk=pk)
    return render(
        reqeust,
        "app/post_detail.html",
        {"post_detail": qs},
    )


post_new = CreateView.as_view(
    model=Post,
    form_class=PostForm,
    success_url="/app/",
)
