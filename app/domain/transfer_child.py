from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy import event, select


class TransferChild(db.Model):
    __tablename__ = 'transfer_child'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kindergarten_from = db.Column(db.Integer, nullable=False)
    kindergarten_to = db.Column(db.Integer, nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"TransferChild(id='{self.id}', kindergarten_from={self.kindergarten_from}, kindergarten_to={self.kindergarten_to}, " \
               f"child_id={self.child_id}, date={self.date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'kindergarten_from': self.kindergarten_from,
            'kindergarten_to': self.kindergarten_to,
            'child_id': self.child_id,
            'date': self.date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TransferChild:
        transfer_child = TransferChild(
            kindergarten_from=dto_dict.get('kindergarten_from'),
            kindergarten_to=dto_dict.get('kindergarten_to'),
            child_id=dto_dict.get('child_id'),
            date=dto_dict.get('date')
        )
        return transfer_child


@event.listens_for(TransferChild, "before_insert")
def check_team_from_to(mapper, connection, target):
    child_table = db.Table('child', db.metadata, autoload_with=db.engine)
    kindergarten_table = db.Table('kindergarten', db.metadata, autoload_with=db.engine)

    child_exists = connection.execute(
        select(child_table.c.id).where(child_table.c.id == target.child_id)
    ).first()

    if not child_exists:
        raise ValueError(f"Child with id {target.child_id} does not exist in child table.")

    kindergarten_from_exists = connection.execute(
        select(kindergarten_table.c.id).where(kindergarten_table.c.id == target.kindergarten_from)
    ).first()

    if not kindergarten_from_exists:
        raise ValueError(f"kindergarten with id {target.kindergarten_from} does not exist in kindergarten table.")

    kindergarten_to_exists = connection.execute(
        select(kindergarten_table.c.id).where(kindergarten_table.c.id == target.kindergarten_to)
    ).first()

    if not kindergarten_to_exists:
        raise ValueError(f"kindergarten with id {target.kindergarten_to} does not exist in kindergarten table.")