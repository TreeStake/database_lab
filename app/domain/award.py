from __future__ import annotations
from app import db
from typing import Dict, Any


class Award(db.Model):
    __tablename__ = 'award'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    money = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Award(id={self.id}, name='{self.name}', money={self.money})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'money': self.money,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Award:
        award = Award(
            name=dto_dict.get('name'),
            money=dto_dict.get('money')
        )
        return award
