from .general_controller import GeneralController
from ..service import dismissal_service


class DismissalController(GeneralController):
    _service = dismissal_service