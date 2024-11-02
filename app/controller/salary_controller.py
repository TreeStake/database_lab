from .general_controller import GeneralController
from ..service import salary_service


class SalaryController(GeneralController):
    _service = salary_service