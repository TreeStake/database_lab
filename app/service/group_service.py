from .general_service import GeneralService
from ..dao import group_dao


class GroupService(GeneralService):
    _dao = group_dao