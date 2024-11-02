from .general_controller import GeneralController
from ..service import kindergarden_service


class KindergartenController(GeneralController):
    _service = kindergarden_service