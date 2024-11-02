from .general_service import GeneralService
from ..dao import educator_has_awards_dao


class EducatorHasAwardsService(GeneralService):
    _dao = educator_has_awards_dao