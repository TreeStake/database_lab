from .general_service import GeneralService
from ..dao import award_dao


class AwardService(GeneralService):
    _dao = award_dao