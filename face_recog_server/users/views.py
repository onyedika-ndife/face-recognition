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


def _clear_stud(request):
    student = STUDENTS.objects.all()

    student.delete()

    return HttpResponse("Cleared Students")


def _clear_staf(request):
    staff = STAFF.objects.all()

    staff.delete()

    return HttpResponse("Cleared Staff")


@api_view(["GET"])
def _staff_all(request):
    staff = STAFF.objects.all()

    serializer = STAFF_SERIALIZERS(staff, many=True, context={"request": request})

    return Response(serializer.data)
