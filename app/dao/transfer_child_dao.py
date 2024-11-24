from .general_dao import GeneralDAO
from ..domain import TransferChild


class TransferChildDAO(GeneralDAO):
    _domain_type = TransferChild