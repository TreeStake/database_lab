from .general_controller import GeneralController
from ..service import child_service


class ChildController(GeneralController):
    _service = child_service