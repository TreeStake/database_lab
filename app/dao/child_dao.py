from .general_dao import GeneralDAO
from ..domain import Child


class ChildDAO(GeneralDAO):
    _domain_type = Child