from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hospitals.forms import HospitalCreateForm, CategoryCreateForm
from hospitals.models import Category, Hospital
from django.contrib import messages
# Create your views here.
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
def hospital_index(request):
    hospital_list = Hospital.objects.all()
    context = {"data": hospital_list}
    if request.method == "POST":
        if not request.POST.get('searchText'):
            return redirect("hospitals")
        filter_data = Hospital.objects.filter(short_name=request.POST.get('searchText'))
        context.update({"filter_data": filter_data, "data": filter_data})
        return render(request, 'hospitals/index.html', context)
    return render(request, 'hospitals/index.html', context)

@login_required(login_url='/authentication/login')
def hospital_edit(request, id):
    data_edit = Hospital.objects.get(id=id)
    categories = Category.objects.all()
    context = {"data": data_edit, "categories": categories}
    return render(request, 'hospitals/edit_hospital.html', context)

@login_required(login_url='/authentication/logout')
def hospital_update(request):
    if request.method == "POST":
        hospital_obj = Hospital.objects.get(id=request.POST.get('id'))
        category = Category.objects.get(id=request.POST.get('category'))
        hospital_obj.full_name = request.POST.get('full_name')
        hospital_obj.short_name = request.POST.get('short_name')
        hospital_obj.address = request.POST.get('address')
        hospital_obj.contact = request.POST.get('contact')
        hospital_obj.category_id = category
        hospital_obj.save()
        messages.success(request, 'Data updated successfully')
        return redirect("hospitals")
    return redirect("hospitals")

@login_required(login_url='/authentication/login')
def hospital_delete(request, id):
    data = Hospital.objects.get(id=id)
    data.delete()
    messages.success(request, 'Data removed!')
    return redirect("hospitals")

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