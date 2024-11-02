from .general_service import GeneralService
from ..dao import dismissal_dao


class DismissalService(GeneralService):
    _dao = dismissal_dao