from .general_controller import GeneralController
from ..service import event_service


class EventController(GeneralController):
    _service = event_service