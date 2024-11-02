from .general_service import GeneralService
from ..dao import event_dao


class EventService(GeneralService):
    _dao = event_dao