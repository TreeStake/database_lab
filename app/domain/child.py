from __future__ import annotations
from app import db
from typing import Dict, Any


class Child(db.Model):
    __tablename__ = 'child'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    kindergarten_id = db.Column(db.Integer, db.ForeignKey('kindergarten.id'), nullable=False)

    def __repr__(self):
        return f"Child(id={self.id}, name='{self.name}', age={self.age}, group_id={self.group_id}, kindergarten_id={self.kindergarten_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'group_id': self.group_id,
            'kindergarten_id': self.kindergarten_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Child:
        child = Child(
            name=dto_dict.get('name'),
            age=dto_dict.get('age'),
            group_id=dto_dict.get('group_id'),
            kindergarten_id=dto_dict.get('kindergarten_id')
        )
        return child
