from .general_service import GeneralService
from ..dao import toy_dao


class ToyService(GeneralService):
    _dao = toy_dao