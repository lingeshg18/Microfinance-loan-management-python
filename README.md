Microfinance Loan Management System
A lightweight microfinance management application built with Python (Tkinter) and MySQL.
Supports 3 user roles (Admin, Staff, Customer) with features for loan processing, EMI payments, repayment tracking, and reporting.

Table of contents
Features

User Roles & Permissions

Technology Stack

Screenshots

Prerequisites

Installation

Database Setup

Configuration

Usage Guide

Project Structure

Contributing

License

Contact

Features
Secure authentication (Admin / Staff / Customer)

Customer registration & profile management

Loan application submission and processing (approve/reject)

Repayment tracking and EMI recording

Payment history and loan status updates (Pending / Ongoing / Completed)

Admin reporting dashboard (loan counts, repayments, overdue)

Role-based UI using Tkinter with custom components

User Roles & Permissions
Admin

Full system control, manage customers, loans, staff accounts, generate reports.

Staff

Process pending loan applications, track repayments, manage assigned customers.

Customer

Register, view loan details, make EMI payments, view payment history.

Technology Stack
Frontend: Python 3.8+, Tkinter (custom UI components)


Backend: MySQL Server

DB Driver: mysql-connector-python

Prerequisites
Python 3.8 or newer

MySQL Server (local or remote)

pip

mysql-connector-python

Database Setup
Start your MySQL server.

Create a database (example microfinance_db) and add three tables (users,loans,repayment).

Run the application:
python main.py

If using a virtual environment, ensure it is activated before running.

Usage Guide
Login Page
Use Admin credentials for full access.

Staff accounts have limited permissions (loan processing, repayment tracking).

Customers can register via the registration form and then log in to apply for loans and make EMI payments.

Admin Panel
Accessed via Admin user.

Sidebar navigation for:

Manage Users (Create / Edit / Delete staff)

Manage Customers (view/edit)

Loans (view pending / approve / reject)

Reports (export loan and payment summaries)

Staff Interface
Process loan applications assigned to the staff.

Record repayments and view assigned customers' loan statuses.

Customer Interface
Register and log in.

View active loans and balances.

Make EMI payments (enter amount and submit; payment recorded with timestamp).

Project Structure:
├── src/
│   ├── auth/               # Authentication (login, hashing, session)
│   ├── db/                 # Database operations (queries, connection pool)
│   ├── gui/                # Tkinter UI components and screens
│   ├── loans/              # Loan processing logic
│   └── reports/            # Report generation & exports
├── database/
│   └── setup.sql           # Database schema & sample data
├── config/
│   └── db_config.ini       # Database configuration (example)
├── docs/
│   └── screenshots/        # UI screenshots for README
└── main.py                 # Entry point
Security Notes & Best Practices
Hash and salt passwords using bcrypt (do not store plaintext).

Use parameterized queries or prepared statements to avoid SQL injection.

Use a connection pool for scalability.

Secure config files (do not commit credentials to public repos).

Consider adding role-based permission checks in business logic (not just UI).
Contributing
Fork the repository

Create a branch: git checkout -b feat/your-feature

Make changes and commit: git commit -m "feat: add ..."

Push to your branch and create a Pull Request

Please follow PEP8 and include unit tests for critical logic (loan calculations, status updates).

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
Maintainer: <Lingesh Kumar G>
Email: <lingeshgy@gmail.com>
Repository: https://github.com/lingeshg18/Microfinance-loan-management-python/tree/main/project

