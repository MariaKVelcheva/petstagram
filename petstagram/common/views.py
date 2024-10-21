from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy
from petstagram.common.models import Like
from petstagram.photos.models import Photo


def show_home_page(request):
    all_photos = Photo.objects.all()
    context = {'all_photos': all_photos}
    return render(request, 'common/home-page.html')





