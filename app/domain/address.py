from __future__ import annotations
from app.database import db
from typing import Dict, Any


class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(45), nullable=False)
    building_number = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"Address(id={self.id}, street='{self.street}', building_number='{self.building_number}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'street': self.street,
            'building_number': self.building_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Address:
        address = Address(
            street=dto_dict.get('street'),
            building_number=dto_dict.get('building_number')
        )
        return address


def insert_addresses(n):
    addresses = [
        Address(
            street=f"No-name{i}",
            building_number=f'{i}'
        )
        for i in range(n)
    ]

    try:
        db.session.bulk_save_objects(addresses)
        db.session.commit()
        return addresses
    except Exception:
        db.session.rollback()
        return -1
