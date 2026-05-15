from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date
from models import db, Author, Book, Member, Loan

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "library-secret-key"

db.init_app(app)


@app.route("/")
def dashboard():
    total_books = Book.query.count()
    total_members = Member.query.count()
    total_loans = Loan.query.count()
    available_books = db.session.query(db.func.sum(Book.available_copies)).scalar() or 0

    return render_template(
        "dashboard.html",
        total_books=total_books,
        total_members=total_members,
        total_loans=total_loans,
        available_books=available_books
    )


@app.route("/books")
def books():
    all_books = Book.query.all()
    return render_template("books.html", books=all_books)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"].strip()
        isbn = request.form["isbn"].strip()
        category = request.form["category"].strip()
        published_year = request.form["published_year"]
        total_copies = request.form["total_copies"]
        author_name = request.form["author_name"].strip()

        if not title or not isbn or not category or not author_name:
            flash("All required fields must be filled.")
            return redirect(url_for("add_book"))

        if int(total_copies) < 0:
            flash("Total copies cannot be negative.")
            return redirect(url_for("add_book"))

        existing_book = Book.query.filter_by(isbn=isbn).first()
        if existing_book:
            flash("Book with this ISBN already exists.")
            return redirect(url_for("add_book"))

        author = Author.query.filter_by(author_name=author_name).first()

        if not author:
            author = Author(author_name=author_name)
            db.session.add(author)
            db.session.flush()

        book = Book(
            title=title,
            isbn=isbn,
            category=category,
            published_year=int(published_year),
            total_copies=int(total_copies),
            available_copies=int(total_copies),
            author_id=author.author_id
        )

        db.session.add(book)
        db.session.commit()
        flash("Book added successfully.")
        return redirect(url_for("books"))

    return render_template("add_book.html")


@app.route("/members")
def members():
    all_members = Member.query.all()
    return render_template("members.html", members=all_members)


@app.route("/add_member", methods=["GET", "POST"])
def add_member():
    if request.method == "POST":
        full_name = request.form["full_name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()

        if not full_name or not email or not phone:
            flash("All member fields are required.")
            return redirect(url_for("add_member"))

        existing_member = Member.query.filter_by(email=email).first()
        if existing_member:
            flash("Member with this email already exists.")
            return redirect(url_for("add_member"))

        member = Member(
            full_name=full_name,
            email=email,
            phone=phone
        )

        db.session.add(member)
        db.session.commit()
        flash("Member added successfully.")
        return redirect(url_for("members"))

    return render_template("add_member.html")


@app.route("/loans")
def loans():
    all_loans = Loan.query.all()
    return render_template("loans.html", loans=all_loans)


@app.route("/issue_book", methods=["GET", "POST"])
def issue_book():
    books = Book.query.filter(Book.available_copies > 0).all()
    members = Member.query.all()

    if request.method == "POST":
        book_id = int(request.form["book_id"])
        member_id = int(request.form["member_id"])

        book = Book.query.get(book_id)
        member = Member.query.get(member_id)

        if not book or not member:
            flash("Invalid book or member selection.")
            return redirect(url_for("issue_book"))

        if book.available_copies <= 0:
            flash("Selected book is not available.")
            return redirect(url_for("issue_book"))

        try:
            loan = Loan(
                book_id=book.book_id,
                member_id=member.member_id,
                loan_date=date.today(),
                status="Issued"
            )

            book.available_copies -= 1

            db.session.add(loan)
            db.session.commit()

            flash("Book issued successfully.")
            return redirect(url_for("loans"))

        except Exception:
            db.session.rollback()
            flash("Transaction failed. Book was not issued.")
            return redirect(url_for("issue_book"))

    return render_template("issue_book.html", books=books, members=members)


@app.route("/return_book/<int:loan_id>")
def return_book(loan_id):
    loan = Loan.query.get_or_404(loan_id)

    if loan.status == "Returned":
        flash("This book is already returned.")
        return redirect(url_for("loans"))

    try:
        loan.status = "Returned"
        loan.return_date = date.today()
        loan.book.available_copies += 1

        db.session.commit()
        flash("Book returned successfully.")

    except Exception:
        db.session.rollback()
        flash("Transaction failed. Book return was not completed.")

    return redirect(url_for("loans"))


if __name__ == "__main__":
    app.run(debug=True)