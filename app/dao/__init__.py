from .adress_dao import AddressDAO
from .award_dao import AwardDAO
from .child_dao import ChildDAO
from .dismissal_dao import DismissalDAO
from .educator_dao import EducatorDAO
from .educator_has_awards_dao import EducatorHasAwardsDAO
from .event_dao import EventDAO
from .group_dao import GroupDAO
from .kindergarden_dao import KindergartenDAO
from .salary_dao import SalaryDAO
from .toy_dao import ToyDAO

address_dao = AddressDAO()
award_dao = AwardDAO()
child_dao = ChildDAO()
dismissal_dao = DismissalDAO()
educator_dao = EducatorDAO()
educator_has_awards_dao = EducatorDAO()
event_dao = EventDAO()
group_dao = GroupDAO()
kindergarden_dao = KindergartenDAO()
salary_dao = SalaryDAO()
toy_dao = ToyDAO()
