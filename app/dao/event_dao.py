from .general_dao import GeneralDAO
from ..domain import Event


class EventDAO(GeneralDAO):
    _domain_type = Event