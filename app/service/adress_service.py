from .general_service import GeneralService
from ..dao import adress_dao


class AddressService(GeneralService):
    _dao = adress_dao