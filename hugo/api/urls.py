from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from hugo.api.views import (
   UserListCreate, UserDetail,
   SalaryList, SalaryDetail,
   EmployeeDetail, EmployeeList, 
   EmploymentList, EmploymentDetail, 
   EmployeeDocsView,EmployeedocsList,
   EducationDetail, EducationList,
   EducationDocsView, EducationdocsList,
   InternDetail, InternList)
from hugo.api.views import ProjectList, ProjectDetail
from hugo.api.views import EventList, EventDetail, HolidayList, HolidayDetail
from hugo.api.views import (TicketList, TicketDetail, 
RequestTicketList, RequestTicketDetail, 
TicketAvailabilityList, TicketAvailabilityDetail)
# Create your urls here.

urlpatterns = [

   path("list/",EmployeeList.as_view(), name="employee_list"),
   path("detail/<int:pk>/",EmployeeDetail.as_view(), name="employee_detail"),

   path("listemployment/",EmploymentList.as_view(), name="employment_list"),
   path("detailemployment/<int:pk>/",EmploymentDetail.as_view(), name="employment_detail"),
   
   path("listeducation/",EducationList.as_view(), name="educationlist"),
   path("detaileducation/<int:pk>/",EducationDetail.as_view(), name="education_detail"),

   path('signin/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
   path('users/',UserListCreate.as_view(), name='usercreate'),
   path('users/me/',UserDetail.as_view(),name='userlist'),
   
   
   path('employment/<int:pk>/employeedoc/',EmployeeDocsView.as_view(), name='employeedoc'), 
   path("docslist/",EmployeedocsList.as_view(), name="employeedocs_list"),

   path('education/<int:pk>/educationdoc/',EducationDocsView.as_view(), name='educationdoc'),
   path("docslist/",EducationdocsList.as_view(), name="educationdocs_list"),

   
   path('listsalary/',SalaryList.as_view(), name='salary'),
   path("detailsalary/<int:pk>/",SalaryDetail.as_view(), name="salary_detail"),

   path("listintern/",InternList.as_view(), name="intern_list"),
   path("detailintern/<int:pk>/",InternDetail.as_view(), name="intern_detail"),

   path("projectlist/",ProjectList.as_view(), name="project_list"),
   path("user/<int:pk>/projectdetail/",ProjectDetail.as_view(), name="project_detail"),

   path("event/",EventList.as_view(),name="event"),
   path("eventset/<int:pk>/",EventDetail.as_view(),name="event_detail"),
   
   path("holiday/",HolidayList.as_view(),name="holiday"),
   path("holidaydetail/<int:pk>/",HolidayDetail.as_view(),name="holiday_detail"),

   path("ticket/",TicketList.as_view(),name="ticket"),
   path("ticketdetail/<int:pk>/",TicketDetail.as_view(),name="ticket_detail"),

   path('ticket/<int:pk>/request/',RequestTicketList.as_view(),name="request_ticket"),
   path("requestlist/",RequestTicketDetail.as_view(), name="request_detail"),

   path('ticket/<int:pk>/availability/',TicketAvailabilityList.as_view(),name="ticket_availability"),
   path("availabilitylist/",TicketAvailabilityDetail.as_view(), name="availability_list"),
   
]
