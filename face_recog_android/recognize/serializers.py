from rest_framework import serializers
from .models import STUDENTS, STAFF


class STUDENT_SERIALIZERS(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = STUDENTS
        fields = (
            "id",
            "last_name",
            "middle_name",
            "first_name",
            "age",
            "level",
            "college",
            "department",
            "matric_number",
            "image",
        )
    def get_image(self, student):
        request = self.context.get('request')
        image = student.pic.url
        return request.build_absolute_uri(image)

class STAFF_SERIALIZERS(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = STAFF
        fields = (
            "id",
            "last_name",
            "middle_name",
            "first_name",
            "age",
            "level",
            "profession",
            "image",
        )

    def get_image(self, staff):
        request = self.context.get('request')
        image = staff.pic.url
        return request.build_absolute_uri(image)
