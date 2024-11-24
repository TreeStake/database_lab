from __future__ import annotations
from app import db
from typing import Dict, Any
from .award import Award
from .educator import Educator


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

    @staticmethod
    def add_award_to_educator(educator_name: str, award_name: int) -> EducatorHasAwards:
        educator = Educator.query.filter_by(name=educator_name).first()
        if not educator:
            raise ValueError("Educator found")

        award = Award.query.filter_by(name=award_name).first()
        if not award:
            raise ValueError("Award not found")

        educator_has_awards = EducatorHasAwards(educators_id=educator.id, awards_id=award.id)
        db.session.add(educator_has_awards)
        db.session.commit()
        return educator_has_awards
