from .general_controller import GeneralController
from ..service import award_service


class AwardController(GeneralController):
    _service = award_service