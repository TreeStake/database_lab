from .general_dao import GeneralDAO
from ..domain import EducatorHasAwards


class EducatorHasAwardsDAO(GeneralDAO):
    _domain_type = EducatorHasAwards