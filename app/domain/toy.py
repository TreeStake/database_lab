from __future__ import annotations
from app import db
from typing import Dict, Any


class Toy(db.Model):
    __tablename__ = 'toy'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    number = db.Column(db.String(45), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    group_educators_id = db.Column(db.Integer, nullable=True)
    group_kindergarten_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Toy(id={self.id}, name='{self.name}', number='{self.number}', group_id={self.group_id}, group_educators_id={self.group_educators_id}, group_kindergarten_id={self.group_kindergarten_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'number': self.number,
            'group_id': self.group_id,
            'group_educators_id': self.group_educators_id,
            'group_kindergarten_id': self.group_kindergarten_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Toy:
        toy = Toy(
            name=dto_dict.get('name'),
            number=dto_dict.get('number'),
            group_id=dto_dict.get('group_id'),
            group_educators_id=dto_dict.get('group_educators_id'),
            group_kindergarten_id=dto_dict.get('group_kindergarten_id')
        )
        return toy
