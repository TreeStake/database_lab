from .general_controller import GeneralController
from ..service import group_service


class GroupController(GeneralController):
    _service = group_service