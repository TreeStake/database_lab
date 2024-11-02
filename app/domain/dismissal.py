from __future__ import annotations
from app import db
from typing import Dict, Any


class Dismissal(db.Model):
    __tablename__ = 'dismissal'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"Dismissal(id={self.id}, date='{self.date}', reason='{self.reason}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'reason': self.reason,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Dismissal:
        dismissal = Dismissal(
            date=dto_dict.get('date'),
            reason=dto_dict.get('reason')
        )
        return dismissal
