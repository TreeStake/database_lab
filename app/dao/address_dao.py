from .general_dao import GeneralDAO
from ..domain import Address


class AddressDAO(GeneralDAO):
    _domain_type = Address