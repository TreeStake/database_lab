from .general_dao import GeneralDAO
from ..domain import Salary


class SalaryDAO(GeneralDAO):
    _domain_type = Salary