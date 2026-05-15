from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = "authors"

    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(100), nullable=False)

    books = db.relationship("Book", backref="author", lazy=True)


class Book(db.Model):
    __tablename__ = "books"

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    isbn = db.Column(db.String(30), unique=True, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)
    total_copies = db.Column(db.Integer, nullable=False)
    available_copies = db.Column(db.Integer, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey("authors.author_id"), nullable=False)

    loans = db.relationship("Loan", backref="book", lazy=True)


class Member(db.Model):
    __tablename__ = "members"

    member_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    membership_date = db.Column(db.Date, default=date.today)

    loans = db.relationship("Loan", backref="member", lazy=True)


class Loan(db.Model):
    __tablename__ = "loans"

    loan_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("members.member_id"), nullable=False)
    loan_date = db.Column(db.Date, default=date.today)
    return_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), default="Issued")