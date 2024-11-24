from __future__ import annotations
from app import db
from typing import Dict, Any
from random import randint, choice
from time import time
from sqlalchemy import text


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    amount = db.Column(db.String(45), nullable=False)
    educators_id = db.Column(db.Integer, db.ForeignKey('educator.id'), nullable=False)
    kindergarten_id = db.Column(db.Integer, db.ForeignKey('kindergarten.id'), nullable=False)
    children = db.relationship('Child', backref='group')
    toys = db.relationship('Toy', backref='group')

    def __repr__(self):
        return f"Group(id={self.id}, name='{self.name}', amount='{self.amount}', educators_id={self.educators_id}, kindergarten_id={self.kindergarten_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        children = [child.put_into_dto() for child in self.children]
        toys = [toy.put_into_dto() for toy in self.toys]
        return {
            'id': self.id,
            'name': self.name,
            'amount': self.amount,
            'educators_id': self.educators_id,
            'kindergarten_id': self.kindergarten_id,
            'children': children if children else None,
            'toys': toys if toys else None
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

def create_dynamic_tables_from_groups():
    groups = Group.query.all()
    if not groups:
        return "No group found in the database."

    created_tables = []

    for group in groups:
        group_name = group.name.replace(" ", "_")
        table_name = f"{group_name}_{int(time())}"

        column_defs = []
        for i in range(randint(1, 9)):
            column_name = f"column_{i + 1}"
            column_type = choice(["INT", "VARCHAR(255)", "DATE"])
            column_defs.append(f"{column_name} {column_type}")
        column_defs_str = ", ".join(column_defs)

        create_table_sql = text(f"CREATE TABLE {table_name} (id INT PRIMARY KEY AUTO_INCREMENT, {column_defs_str});")

        db.session.execute(create_table_sql)
        db.session.commit()
        created_tables.append(table_name)

    return created_tables