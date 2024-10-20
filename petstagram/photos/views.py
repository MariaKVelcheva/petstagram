from django.shortcuts import render


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, photo_id):
    return render(request, 'photos/photo-details-page.html')


def photo_edit(request, photo_id):
    return render(request, 'photos/photo-edit-page.html')


