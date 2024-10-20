from django.shortcuts import render


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, pet_id):
    return render(request, 'pets/pet-details-page.html')


def pet_edit(request, pet_id):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete(request, pet_id):
    return render(request, 'pets/pet-delete-page.html')


