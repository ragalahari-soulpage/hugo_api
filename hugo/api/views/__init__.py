from .users import UserListCreate, UserDetail,  SalaryList, SalaryDetail
from .employee import (
 EmployeeList, EmployeeDetail,
 EmploymentList, EmploymentDetail, 
 EmployeeDocsView, EmployeedocsList,
 EducationList, EducationDetail,
 EducationDocsView, EducationdocsList,
 InternDetail, InternList
)
from .project import ProjectList, ProjectDetail
from .library import EventList, EventDetail, HolidayList, HolidayDetail
from .ticket import (
    TicketDetail, TicketList, RequestTicketList, RequestTicketDetail, TicketAvailabilityList, TicketAvailabilityDetail
)