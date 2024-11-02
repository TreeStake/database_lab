from .general_controller import GeneralController
from ..service import toy_service


class ToyController(GeneralController):
    _service = toy_service