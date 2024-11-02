from .general_service import GeneralService
from ..dao import kindergarden_dao


class KindergardenService(GeneralService):
    _dao = kindergarden_dao