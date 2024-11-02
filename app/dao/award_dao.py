from .general_dao import GeneralDAO
from ..domain import Award


class AwardDAO(GeneralDAO):
    _domain_type = Award