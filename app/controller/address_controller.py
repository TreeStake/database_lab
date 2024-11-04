from .general_controller import GeneralController
from ..service import address_service


class AddressController(GeneralController):
    _service = address_service