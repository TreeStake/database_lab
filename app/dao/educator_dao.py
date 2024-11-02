from .general_dao import GeneralDAO
from ..domain import Educator


class EducatorDAO(GeneralDAO):
    _domain_type = Educator