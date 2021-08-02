from django.db import models
from .user import User

class Employee(models.Model):
    
   # User model as Foreign Key
   user = models.ForeignKey(User, on_delete=models.CASCADE)

   # Employee date of birth
#    date_of_birth = models.DateField(blank=True)
    
   first_name = models.CharField( max_length=10, blank=True)
   last_name = models.CharField( max_length=10, blank=True)
   # gender
   gender = models.CharField( max_length=10, blank=True)

   # blood group
   blood_group = models.CharField(max_length=255, blank=True)

   # aadhar number
   aadhar_number = models.CharField(max_length=12, blank=True)

   # pan number
   pan_number = models.CharField(max_length=10, blank=True)

   # permanent address
   permanent_address = models.TextField(blank=True)

   # current address
   current_address = models.TextField(blank=True)

   # Employee avatar
#    avatar = models.FileField(
#        upload_to="hugo_users/", blank=True, default="hugo_users/default-user-icon.svg"
#    )

   # contact Info
   # alternate email/ personal email
   personal_email = models.EmailField(max_length=255, blank=True)

   # Employee contact number
   phone = models.CharField(max_length=10, unique=True, blank=True)

   # Employee alternate contact number
   alternate_phone = models.CharField(max_length=10, blank=True)

   # emergency contact person
   emergency_contact_person = models.CharField(max_length=255, blank=True)

   # emergency contact number
   emergency_contact_number = models.CharField(max_length=10, blank=True)

   # Job Info issued by HR
   # Employee ID
   emp_id = models.CharField(max_length=10, blank=True)

   # Employee date of joining in the company
   date_of_joined = models.DateField(blank=True, null=True)

   # Employee date of relieving in the company
   last_working_date = models.DateField(blank=True, null=True)

   # laptop serial number given to employee
   device_serial_number = models.CharField(max_length=255, blank=True)

   # team
#    team = models.ForeignKey(
#        "TeamInfo", on_delete=models.SET_NULL, blank=True, null=True
#    )

   # reporting supervisor
   reporting = models.CharField(max_length=255, blank=True)

   # designation
   designation = models.CharField(max_length=255, blank=True)

   # division
   division = models.CharField(max_length=255, blank=True)

   # employee status
   is_active = models.BooleanField(default=True)
    
   class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employee"
        db_table = "employee"

   def __str__(self):
        return self.user

class Employment(models.Model):
    
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Employment"
        verbose_name_plural = "Employment"
        db_table = "employment"

    def __str__(self):
        return self.employee_id
    
class EmployeeDocs(models.Model):
    
    # employeeid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    docs = models.FileField(upload_to= 'docs')
    
    
    class Meta:
        verbose_name = "EmployeeDocs"
        verbose_name_plural = "EmployeeDocs"
        db_table = "employeedocs"

    def __str__(self):
        return self.employment

class Education(models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=255, blank=True)
    degree = models.CharField(max_length=255, blank=True)
    specialization = models.CharField(max_length=255, blank=True)
    institution = models.CharField(max_length=255, blank=True)
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        db_table = "education"

    def __str__(self):
        return self.employee

class EducationDocs(models.Model):
    
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    docs = models.FileField(upload_to= 'docs')
    
    
    class Meta:
        verbose_name = "EducationDocs"
        verbose_name_plural = "EduactionDocs"
        db_table = "educationdocs"

    def __str__(self):
        return self.education


class Internship(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    intern_name = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Internship"
        verbose_name_plural = "Internship"
        db_table ="internship"

    def __str__(self):

        return self.title


