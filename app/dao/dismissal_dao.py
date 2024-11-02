from .general_dao import GeneralDAO
from ..domain import Dismissal


class DismissalDAO(GeneralDAO):
    _domain_type = Dismissal