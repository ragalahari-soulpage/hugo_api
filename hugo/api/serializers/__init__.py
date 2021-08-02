from  .user import UserSerializer, SalarySerializer
from .employee import (
    EmployeeSerializer,
    EmploymentSerializer, EmployeeDocsSerializer,
    EducationSerializer, EducationDocsSerializer,
    InternshipSerializer
)
from .project import ProjectSerializer
from .library import EventSerializer, HolidaySerializer
from .ticket import TicketSerializer, RequestTicketSerializer, TicketAvailabilitySerializer