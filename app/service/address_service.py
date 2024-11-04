from .general_service import GeneralService
from ..dao import address_dao


class AddressService(GeneralService):
    _dao = address_dao