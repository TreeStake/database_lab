from .general_dao import GeneralDAO
from ..domain import Toy


class ToyDAO(GeneralDAO):
    _domain_type = Toy