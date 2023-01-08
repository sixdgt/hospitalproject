from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hospitals.forms import HospitalCreateForm, CategoryCreateForm
from hospitals.models import Category, Hospital

# Create your views here.
@login_required(login_url='/authentication/login/')
def hospital_index(request):
    return render(request, 'hospitals/index.html')

@login_required(login_url='/authentication/login')
def category_create(request):
    create_form = CategoryCreateForm()
    context = {"form": create_form}

    if request.method == "POST":
        # req_category = request.POST.get('category')
        # req_category_code = request.POST.get('category_code')
        # category = Category(category=req_category, category_code=req_category_code)
        # category.save()
        form_data = CategoryCreateForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("hospitals")
        else:
            return redirect("category.create")

    return render(request, 'categories/add_category.html', context)

@login_required(login_url='/authentication/login/')
def hospital_create(request):
    create_form = HospitalCreateForm()
    context = {"form": create_form}
    if request.method == "POST":
        form_data = HospitalCreateForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("hospitals")
        else:
            return redirect("hospital.create")
    return render(request, 'hospitals/add_hospital.html', context)