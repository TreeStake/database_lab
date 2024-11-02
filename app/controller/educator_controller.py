from .general_controller import GeneralController
from ..service import educator_service


class EducatorController(GeneralController):
    _service = educator_service