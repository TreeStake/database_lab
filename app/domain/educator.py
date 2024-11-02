from __future__ import annotations
from app import db
from typing import Dict, Any
from datetime import datetime


class Educator(db.Model):
    __tablename__ = 'educator'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    kindergarten_id = db.Column(db.Integer, db.ForeignKey('kindergarten.id'), nullable=False)
    hire = db.Column(db.Date, nullable=False)
    salary_id = db.Column(db.Integer, db.ForeignKey('salary.id'), nullable=False)
    dismissal_id = db.Column(db.Integer, db.ForeignKey('dismissal.id'), nullable=True)

    def __repr__(self):
        return (f"Educator(id={self.id}, name='{self.name}', surname='{self.surname}', hire='{self.hire}', "
                f"salary_id='{self.salary_id}')")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'kindergarten_id': self.kindergarten_id,
            'hire': self.hire.isoformat() if self.hire else None,  # форматування дати
            'salary_id': self.salary_id,
            'dismissal_id': self.dismissal_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Educator:
        educator = Educator(
            name=dto_dict.get('name'),
            surname=dto_dict.get('surname'),
            kindergarten_id=dto_dict.get('kindergarten_id'),
            hire=dto_dict.get('hire'),  # переконайтеся, що дата у правильному форматі
            salary_id=dto_dict.get('salary_id'),
            dismissal_id=dto_dict.get('dismissal_id')
        )
        return educator
