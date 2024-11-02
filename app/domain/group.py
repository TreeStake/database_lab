from __future__ import annotations
from app import db
from typing import Dict, Any


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    amount = db.Column(db.String(45), nullable=False)
    educators_id = db.Column(db.Integer, db.ForeignKey('educator.id'), nullable=False)
    kindergarten_id = db.Column(db.Integer, db.ForeignKey('kindergarten.id'), nullable=False)

    def __repr__(self):
        return f"Group(id={self.id}, name='{self.name}', amount='{self.amount}', educators_id={self.educators_id}, kindergarten_id={self.kindergarten_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'amount': self.amount,
            'educators_id': self.educators_id,
            'kindergarten_id': self.kindergarten_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Group:
        group = Group(
            name=dto_dict.get('name'),
            amount=dto_dict.get('amount'),
            educators_id=dto_dict.get('educators_id'),
            kindergarten_id=dto_dict.get('kindergarten_id')
        )
        return group
