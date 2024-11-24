from __future__ import annotations
from app import db
from typing import Dict, Any


class Salary(db.Model):
    __tablename__ = 'salary'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"Salary(id={self.id}, amount={self.amount}, experience='{self.experience}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'amount': self.amount,
            'experience': self.experience,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Salary:
        salary = Salary(
            amount=dto_dict.get('amount'),
            experience=dto_dict.get('experience')
        )
        return salary

def get_through_salary(salary_type):
    if salary_type == 'MAX':
        result = db.session.query(db.func.max(Salary.amount)).scalar()
        return result
    elif salary_type == 'MIN':
        result = db.session.query(db.func.min(Salary.amount)).scalar()
        return result
    elif salary_type == 'SUM':
        result = db.session.query(db.func.sum(Salary.amount)).scalar()
        return result
    elif salary_type == 'AVG':
        result = db.session.query(db.func.avg(Salary.amount)).scalar()
        return result
    else:
        return -1