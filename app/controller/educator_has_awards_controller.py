from .general_controller import GeneralController
from ..service import educator_has_awards_service


class EducatorHasAwardsController(GeneralController):
    _service = educator_has_awards_service