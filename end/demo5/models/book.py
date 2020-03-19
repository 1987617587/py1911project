from .utils import *
from sqlalchemy.orm import relationship, backref


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    c_id = db.Column("cid", db.ForeignKey("category.id", ondelete='CASCADE'), nullable=False)
    category = db.relationship("Category", backref="books")

    def __repr__(self):
        return self.name


class Category(db.Model):
    # id = db.Colum(name="id", type=db.Integer(), primary_key=True, autoincrement=True)
    # name = db.Colum(name="id", type=db.String(50), nullable=False, unique=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return self.name

