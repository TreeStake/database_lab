from .general_controller import GeneralController
from ..service import adress_service


class AdressController(GeneralController):
    _service = adress_service