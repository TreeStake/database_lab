from .general_service import GeneralService
from ..dao import salary_dao


class SalaryService(GeneralService):
    _dao = salary_dao