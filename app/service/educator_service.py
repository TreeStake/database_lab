from .general_service import GeneralService
from ..dao import educator_dao


class EducatorService(GeneralService):
    _dao = educator_dao