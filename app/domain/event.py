from __future__ import annotations
from app import db
from typing import Dict, Any


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    date = db.Column(db.Date, nullable=False)
    educators_id = db.Column(db.Integer, db.ForeignKey('educator.id'), nullable=False)
    educators_kindergarten_id = db.Column(db.Integer, db.ForeignKey('educator.kindergarten_id'), nullable=False)

    def __repr__(self):
        return f"Event(id={self.id}, name='{self.name}', date={self.date}, educators_id={self.educators_id}, educators_kindergarten_id={self.educators_kindergarten_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date.isoformat(),
            'educators_id': self.educators_id,
            'educators_kindergarten_id': self.educators_kindergarten_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Event:
        event = Event(
            name=dto_dict.get('name'),
            date=dto_dict.get('date'),
            educators_id=dto_dict.get('educators_id'),
            educators_kindergarten_id=dto_dict.get('educators_kindergarten_id')
        )
        return event
