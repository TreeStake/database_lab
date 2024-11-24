from .general_service import GeneralService
from ..dao import transfer_child_dao


class TransferChildService(GeneralService):
    _dao = transfer_child_dao