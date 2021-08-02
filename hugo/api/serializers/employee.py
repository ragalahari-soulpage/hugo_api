from hugo.db.models.employee import (
    EmployeeDocs,
    Employment,
    Education, 
    EducationDocs,
    Internship)

from rest_framework import serializers
from hugo.db.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
       class Meta:
        model = Employee
    #     fields = (
    #     #    "id",
    #     #    "user",
    #     #    "date_of_birth",
    #        "first_name",
    #        "last_name",
    #        "gender",
    #        "blood_group",
    #        "aadhar_number",
    #        "pan_number",
    #        "permanent_address",
    #        "current_address",
    #     #    "avatar",
    #        "personal_email",
    #        "phone",
    #        "alternate_phone",
    #        "emergency_contact_person",
    #        "emergency_contact_number",
    #     #    "facial_reference",
    #    )
        fields = "__all__"

class EmploymentSerializer(serializers.ModelSerializer):

      class Meta:
          model = Employment
          fields = "__all__"

class EmployeeDocsSerializer(serializers.ModelSerializer):
    
      class Meta:
          model = EmployeeDocs
          fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):
    
      class Meta:
          model = Education
          fields = "__all__"

class EducationDocsSerializer(serializers.ModelSerializer):
    
      class Meta:
          model = EducationDocs
          fields = "__all__"

class InternshipSerializer(serializers.ModelSerializer):
    
      class Meta:
          model = Internship
          fields = "__all__"