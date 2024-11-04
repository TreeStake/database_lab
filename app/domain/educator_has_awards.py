from __future__ import annotations
from app import db
from typing import Dict, Any


class EducatorHasAwards(db.Model):
    __tablename__ = 'educator_has_awards'

    educators_id = db.Column(db.Integer, db.ForeignKey('educator.id'), primary_key=True)
    awards_id = db.Column(db.Integer, db.ForeignKey('award.id'), primary_key=True)

    def __repr__(self):
        return f"EducatorHasAwards(educators_id={self.educators_id}, awards_id={self.awards_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'educators_id': self.educators_id,
            'awards_id': self.awards_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EducatorHasAwards:
        educator_has_awards = EducatorHasAwards(
            educators_id=dto_dict.get('educators_id'),
            awards_id=dto_dict.get('awards_id')
        )
        return educator_has_awards
