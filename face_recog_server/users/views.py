from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import STUDENTS, STAFF
from .serializers import STUDENT_SERIALIZERS, STAFF_SERIALIZERS

# Create your views here.
@api_view(["GET"])
def _student_all(request):
    students = STUDENTS.objects.all()

    serializer = STUDENT_SERIALIZERS(students, many=True, context={"request": request})

    return Response(serializer.data)


@api_view(["GET"])
def _staff_all(request):
    staff = STAFF.objects.all()

    serializer = STAFF_SERIALIZERS(staff, many=True, context={"request": request})

    return Response(serializer.data)


@api_view(["PUT"])
def _update_stud(request, pk):
    if request.method == "POST":
        student = STUDENTS.objects.get(pk=pk)

        student.first_name = request.POST.get("first_name")
        student.middle_name = request.POST.get("middle_name")
        student.last_name = request.POST.get("last_name")
        student.date_of_birth = request.POST.get("date_of_birth")
        student.age = request.POST.get("age")
        student.gender = request.POST.get("gender")
        student.nationality = request.POST.get("nationality")
        student.state_of_origin = request.POST.get("state_of_origin")
        student.lga_origin = request.POST.get("lga_origin")
        student.marital_status = request.POST.get("marital_status")
        student.jamb_number = request.POST.get("jamb_number")
        student.college = request.POST.get("college")
        student.department = request.POST.get("department")
        student.level = request.POST.get("level")
        student.matric_number = request.POST.get("matric_number")
        student.address = request.POST.get("address")
        student.phone_number = request.POST.get("phone_number")
        student.email = request.POST.get("email")
        student.parent_name = request.POST.get("parent_name")
        student.parent_email = request.POST.get("parent_email")
        student.parent_phone = request.POST.get("parent_phone")
        student.date_of_registration = request.POST.get("date_of_registration")

        student.save()

        return HttpResponse("Student Profile Updated!")


@api_view(["PUT"])
def _update_staf(request, pk):
    if request.method == "POST":
        staff = STAFF.objects.get(pk=pk)

        staff.first_name = request.POST.get("first_name")
        staff.middle_name = request.POST.get("middle_name")
        staff.last_name = request.POST.get("last_name")
        staff.date_of_birth = request.POST.get("date_of_birth")
        staff.age = request.POST.get("age")
        staff.gender = request.POST.get("gender")
        staff.nationality = request.POST.get("nationality")
        staff.state_of_origin = request.POST.get("state_of_origin")
        staff.lga_origin = request.POST.get("lga_origin")
        staff.marital_status = request.POST.get("marital_status")
        staff.profession = request.POST.get("profession")
        staff.address = request.POST.get("address")
        staff.phone_number = request.POST.get("phone_number")
        staff.email = request.POST.get("email")
        staff.date_of_registration = request.POST.get("date_of_registration")

        staff.save()

        return HttpResponse("Staff Updated!")
