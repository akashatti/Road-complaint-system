from django.shortcuts import render, redirect, get_object_or_404
from .models import Complaint


def home(request):
    return render(request, 'complaints/home.html')


def complaint_list(request):
    complaints = Complaint.objects.all().order_by('-date_reported')
    return render(
        request,
        'complaints/complaint_list.html',
        {'complaints': complaints}
    )


def add_complaint(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        problem = request.POST['problem']
        description = request.POST['description']

        Complaint.objects.create(
            name=name,
            location=location,
            problem=problem,
            description=description
        )

        return redirect('complaint_list')

    return render(request, 'complaints/add_complaint.html')


def complaint_detail(request, id):
    complaint = get_object_or_404(Complaint, id=id)

    return render(
        request,
        'complaints/complaint_detail.html',
        {'complaint': complaint}
    )


def delete_complaint(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    complaint.delete()

    return redirect('complaint_list')