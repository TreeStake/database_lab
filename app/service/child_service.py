from .general_service import GeneralService
from ..dao import child_dao


class ChildService(GeneralService):
    _dao = child_dao