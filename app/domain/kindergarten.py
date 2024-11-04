from __future__ import annotations
from app import db
from typing import Dict, Any


class Kindergarten(db.Model):
    __tablename__ = 'kindergarten'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(45), nullable=False)
    adress_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    groups = db.relationship('Group', backref='kindergarten')
    educators = db.relationship('Educator', backref='kindergarten')

    def __repr__(self):
        return f"Kindergarten(id={self.id}, number='{self.number}', adress_id={self.adress_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        groups = [group.put_into_dto() for group in self.groups]
        educators = [educator.put_into_dto() for educator in self.educators]
        return {
            'id': self.id,
            'number': self.number,
            'adress_id': self.adress_id,
            'groups': groups if groups else None,
            'educators': educators if educators else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Kindergarten:
        kindergarten = Kindergarten(
            number=dto_dict.get('number'),
            adress_id=dto_dict.get('adress_id')
        )
        return kindergarten
