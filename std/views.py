
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Students, Fees


def home(request):
    students = Students.objects.all()
    return render(request, "std/home.html", {"std": students})


@transaction.atomic
def std_add(request):
    if request.method == "POST":
        student = Students(
            roll=request.POST.get("std_roll"),
            name=request.POST.get("std_name"),
            email=request.POST.get("std_email"),
            address=request.POST.get("std_address"),
            phone=request.POST.get("std_phone"),
        )

        try:
            student.full_clean()
            student.save()

            fees = Fees(
                student=student,
                total_fees=request.POST.get("total_fees"),
                paid_amount=request.POST.get("paid_amount"),
            )

            fees.full_clean()
            fees.save()

            return redirect("home")

        except ValidationError as e:
            if student.pk:
                student.delete()

            error_list = []
            if hasattr(e, "message_dict"):
                for msgs in e.message_dict.values():
                    error_list.extend(msgs)
            else:
                error_list.extend(e.messages)

            error_message = ", ".join(error_list)

            return render(request, "std/add_std.html", {
                "error": error_message
            })

    return render(request, "std/add_std.html")


@transaction.atomic
def delete_std(request, id):
    student = get_object_or_404(Students, id=id)
    student.delete()
    return redirect("home")


def update_std(request, id):
    student = get_object_or_404(Students, id=id)
    return render(request, "std/update_std.html", {"std": student})


@transaction.atomic
def do_update_std(request, id):
    student = get_object_or_404(Students, id=id)

    try:
        student.roll = request.POST.get("std_roll")
        student.name = request.POST.get("std_name")
        student.email = request.POST.get("std_email")
        student.address = request.POST.get("std_address")
        student.phone = request.POST.get("std_phone")
        student.full_clean()   
        student.save()

        fees = student.fees
        fees.total_fees = request.POST.get("total_fees")
        fees.paid_amount = request.POST.get("paid_amount")
        fees.full_clean()      
        fees.save()

        return redirect("home")

    except ValidationError as e:
      if hasattr(e, "message_dict"):
        
        error_list = []
        for messages in e.message_dict.values():
            error_list.extend(messages)
        error_message = ", ".join(error_list)
    else:
        error_message = ", ".join(e.messages)

    return render(request, "std/add_std.html", {
        "error": error_message
    })