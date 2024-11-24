from .general_controller import GeneralController
from ..service import transfer_child_service


class TransferChildController(GeneralController):
    _service = transfer_child_service