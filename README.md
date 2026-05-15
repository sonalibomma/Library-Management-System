# Library Management System

## Project Description

The Library Management System is a full-stack web application developed using Flask, SQLAlchemy, SQLite, HTML5, CSS3, Bootstrap, and Jinja2 templates. The system is designed to manage library operations including book management, member registration, loan tracking, and transaction handling.

The application provides a professional and user-friendly interface for librarians to efficiently maintain library records while ensuring proper database normalization and data integrity.

This project was developed as part of CS665 Project 3 and demonstrates concepts related to:
- Full-stack web development
- Relational database management
- Third Normal Form (3NF)
- CRUD operations
- Transaction management
- Server-side validation
- Version control using Git and GitHub

------------------------------------------------------------

# Features

## Dashboard Analytics
The dashboard provides real-time summary statistics including:
- Total number of books
- Total number of members
- Total number of loans
- Total available book copies

The dashboard uses SQL aggregate functions such as:
- COUNT()
- SUM()

------------------------------------------------------------

## Book Management
The system allows users to:
- Add new books
- View all books
- Store ISBN information
- Manage available copies
- Associate books with authors

------------------------------------------------------------

## Member Management
The system allows users to:
- Register members
- Store contact information
- Maintain membership records

------------------------------------------------------------

## Loan Management
The system supports:
- Issuing books
- Returning books
- Updating loan status
- Tracking return dates
- Automatically updating available copies

------------------------------------------------------------

## Transaction Logic
Transaction handling is implemented to ensure database consistency.

Examples:
- Book availability decreases only after successful loan creation
- Book availability increases after successful return processing
- Failed transactions are rolled back automatically

------------------------------------------------------------

## Data Validation
Server-side validation prevents invalid data from entering the database.

Validation includes:
- Required field validation
- Duplicate ISBN prevention
- Duplicate member email prevention
- Restriction of negative copy counts

------------------------------------------------------------

# Technologies Used

## Backend
- Python 3
- Flask
- Flask-SQLAlchemy

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- Jinja2 Templates

## Database
- SQLite

## Version Control
- Git
- GitHub

------------------------------------------------------------

# Database Design

The database consists of the following normalized tables:

## Authors
Stores author details.

## Books
Stores:
- Title
- ISBN
- Category
- Published year
- Copy availability

## Members
Stores:
- Member information
- Email
- Phone number
- Membership date

## Loans
Tracks:
- Loan transactions
- Return status
- Loan dates
- Return dates

------------------------------------------------------------

# Database Relationships

The application implements:
- One-to-Many relationship between Authors and Books
- One-to-Many relationship between Members and Loans
- One-to-Many relationship between Books and Loans

------------------------------------------------------------

# Third Normal Form (3NF)

The database schema was analyzed and normalized to Third Normal Form (3NF).

The normalization process includes:
- Functional dependency analysis
- Removal of redundancy
- Elimination of update anomalies
- Final normalized relational schema

Detailed normalization documentation is included in:

NORMALIZATION.md

------------------------------------------------------------

# Project Structure

library_management_system/

│

├── static/
│   ├── css/
│   └── images/

├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── books.html
│   ├── add_book.html
│   ├── members.html
│   ├── add_member.html
│   ├── loans.html
│   └── issue_book.html

├── app.py
├── models.py
├── schema.sql
├── requirements.txt
├── README.md
├── AI_LOG.md
├── NORMALIZATION.md
└── .gitignore

------------------------------------------------------------

# Installation Instructions

## Step 1 — Clone Repository

git clone https://github.com/sonalibomma/Library-Management-System.git

------------------------------------------------------------

## Step 2 — Navigate to Project Directory

cd Library-Management-System

------------------------------------------------------------

## Step 3 — Create Virtual Environment

python -m venv venv

------------------------------------------------------------

## Step 4 — Activate Virtual Environment

Windows:

venv\Scripts\activate

------------------------------------------------------------

## Step 5 — Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------

# Database Setup

The SQL schema is provided in:

schema.sql

To initialize the database:

from app import app
from models import db

with app.app_context():
    db.create_all()

The SQLite database file will be automatically created.

------------------------------------------------------------

# Running the Application

Start the Flask application:

python app.py

Open browser:

http://127.0.0.1:5000

------------------------------------------------------------

# Functional Workflow

## Adding Books
Users can:
1. Open Add Book page
2. Enter book details
3. Save records into database

------------------------------------------------------------

## Registering Members
Users can:
1. Open Add Member page
2. Enter member details
3. Store records securely

------------------------------------------------------------

## Issuing Books
Users can:
1. Select available books
2. Select registered members
3. Create loan transaction
4. Automatically decrease available copies

------------------------------------------------------------

## Returning Books
Users can:
1. Open Loans page
2. Click Return
3. Update loan status
4. Restore available book copies

------------------------------------------------------------

# Sample Test Data

## Sample Book

Title: Database System Concepts
ISBN: ISBN1001
Author: Abraham Silberschatz
Category: Database
Published Year: 2020
Total Copies: 5

------------------------------------------------------------

## Sample Member

Full Name: John Smith
Email: john.smith@example.com
Phone: 3165551234

------------------------------------------------------------

# GitHub Repository

https://github.com/sonalibomma/Library-Management-System

------------------------------------------------------------

# Git Commit History

The project maintains incremental Git commit history demonstrating:
- Database development
- Backend implementation
- Frontend template creation
- Documentation updates
- Dependency management

------------------------------------------------------------

# AI Usage Disclosure

Generative AI tools were used as development assistants during:
- Project planning
- Backend guidance
- Frontend template generation
- Documentation support

All generated outputs were reviewed, modified, tested, and validated before final integration.

Complete disclosure is available in:

AI_LOG.md

------------------------------------------------------------

# Screenshots Included

The project includes screenshots demonstrating:
- Dashboard
- Books page
- Members page
- Loans page
- Add Book page
- Issue Book page

------------------------------------------------------------

# Author

Sonali Bomma

CS665 — Project 3
Library Management System

------------------------------------------------------------

# Conclusion

The Library Management System successfully demonstrates the implementation of a normalized relational database with a professional Flask-based full-stack application. The project includes CRUD functionality, transaction handling, dashboard analytics, validation mechanisms, Git version control, and complete technical documentation.