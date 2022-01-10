# virtualBookshelf.py
#
# Python Bootcamp Day 63 - Virtual Bookshelf
# Usage:
#     A Flask App that helps you track and rate books in your library.
#     Day 63 Python Bootcamp.
#
# Marceia Egler January 10, 2021

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import Book
import secrets

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=secrets.token_urlsafe(16),
    SQLALCHEMY_DATABASE_URI="sqlite:///new-books-collection.db",
)
db = SQLAlchemy(app)
Bootstrap(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route("/")
def home():
    all_books = Books.query.all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    book = Book()
    book_title = book.book_name
    book_author = book.book_author
    book_rating = book.book_rating
    id = Books.id
    if request.method == "POST":
        if book.validate_on_submit():
            add_book = Books(title=book_title.data,
                             author=book_author.data,
                             rating=book_rating.data)
            db.session.add(add_book)
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("add.html", form=book)


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    book_to_update = Books.query.get(id)
    if request.method == "POST":
        book_to_update.rating = request.form["books_rating"]
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", id=id, book=book_to_update)


@app.route("/delete/<id>")
def delete(id):
    book_to_delete = Books.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return render_template("index.html", id=id)


if __name__ == "__main__":
    app.run(debug=True)
