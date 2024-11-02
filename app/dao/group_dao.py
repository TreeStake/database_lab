from .general_dao import GeneralDAO
from ..domain import Group


class GroupDAO(GeneralDAO):
    _domain_type = Group