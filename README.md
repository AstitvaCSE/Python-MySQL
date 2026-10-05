# Python-MySQL
python-MySQL connectivity program performing CRUD operations
# 🏏 HPL Database Management System

### VIT Hostel Premier League — Technical Department Recruitment

A Python–MySQL database management project developed as part of the **Database Management Team recruitment for VIT's Hostel Premier League (HPL) Technical Department**.

This project demonstrates the integration of a Python application with a MySQL relational database to perform fundamental **CRUD (Create, Read, Update, Delete)** operations.

---

## 📌 Project Overview

The objective of this project is to demonstrate practical understanding of:

- Python–MySQL connectivity
- Relational database management
- SQL queries
- CRUD operations
- Database-driven Python applications
- Basic data management and manipulation

The application provides a simple command-line interface through which student/player records can be created, viewed, updated, and deleted.

---

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3** | Application development |
| **MySQL 8.4 LTS** | Relational database |
| **MySQL Workbench** | Database management and SQL execution |
| **MySQL Connector/Python** | Python–MySQL connectivity |
| **Git & GitHub** | Version control and project hosting |

---

## 🗄️ Database Structure

The project uses a database named:

```text
school
```

with a table named:

```text
student
```

### Student Table

| Column | Data Type | Description |
|---|---|---|
| `roll_no` | INT | Unique student/record identifier |
| `name` | VARCHAR(30) | Name of the student |
| `marks` | INT | Marks associated with the record |

The `roll_no` field is used as the **Primary Key**.

---

## 🔄 CRUD Operations

The application implements all four fundamental database operations.

### 1. Create

Adds a new record to the database using the SQL `INSERT` statement.

```sql
INSERT INTO student VALUES (...);
```

### 2. Read

Retrieves and displays existing records using the SQL `SELECT` statement.

```sql
SELECT * FROM student;
```

### 3. Update

Modifies an existing record using the SQL `UPDATE` statement.

```sql
UPDATE student SET marks = ... WHERE roll_no = ...;
```

### 4. Delete

Removes a record using the SQL `DELETE` statement.

```sql
DELETE FROM student WHERE roll_no = ...;
```

---

## 🔌 Python–MySQL Connectivity

The application uses `mysql-connector-python` to establish communication between Python and MySQL.

Example:

```python
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="school"
)
```

A MySQL cursor is then used to execute SQL queries:

```python
cur = con.cursor()
cur.execute(query, data)
```

Changes made through `INSERT`, `UPDATE`, and `DELETE` operations are committed using:

```python
con.commit()
```

---

## 📁 Project Structure

```text
HPL-Database-Management/
│
├── python-sql_testprogram.py
├── database.sql
└── README.md
```

### `python-sql_testprogram.py`

Contains the main Python application and implements the CRUD operations.

### `database.sql`

Contains the SQL commands required to create the database and table.

### `README.md`

Provides documentation, setup instructions, and an overview of the project.

---

## 🚀 Setup & Installation

### 1. Install Python

Install Python 3 from the official Python website.

Verify the installation:

```bash
python --version
```

### 2. Install MySQL

Install **MySQL Community Server 8.4 LTS** and MySQL Workbench.

Make sure the MySQL Server is running before executing the Python program.

### 3. Install MySQL Connector/Python

Run:

```bash
pip install mysql-connector-python
```

### 4. Create the Database

Open MySQL Workbench and execute the contents of:

```text
database.sql
```

This creates the required database and table.

### 5. Configure the Python Program

Open:

```text
python-sql_testprogram.py
```

Replace:

```python
password="YOUR_MYSQL_PASSWORD"
```

with your local MySQL `root` password.

**Do not upload your actual password to GitHub.**

### 6. Run the Application

Execute:

```bash
python python-sql_testprogram.py
```

---

## 🖥️ Application Menu

The program provides a simple menu-driven interface:

```text
===== STUDENT DATABASE =====

1. Create
2. Read
3. Update
4. Delete
5. Exit
```

Users can select an operation and interact with the database through the terminal.

---

## 🎯 Relevance to HPL Technical Department

Although this project uses a simple student database for demonstration, the same architecture can be extended to an actual **Hostel Premier League database system**.

Potential applications include:

- Player registration
- Team management
- Player statistics
- Match records
- Tournament fixtures
- Points tables
- Player performance tracking
- Team rosters
- Match results
- Database-backed dashboards

A larger implementation could connect these components through multiple relational tables and foreign-key relationships.

---

## 🔮 Future Improvements

Possible extensions include:

- Player and team tables
- Match scheduling system
- Automated points table
- Player statistics and leaderboards
- Search and filtering functionality
- Data validation
- Foreign-key relationships
- Admin authentication
- GUI using Tkinter
- Web-based interface
- REST API integration
- Automated reporting and analytics

---

## 📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

- Python programming
- SQL fundamentals
- Relational databases
- MySQL database management
- Python database connectivity
- CRUD operations
- SQL query execution
- Database transactions
- Basic software project organization
- GitHub-based version control

---

## 👨‍💻 Project Purpose

This project was developed as a **technical demonstration for the VIT Hostel Premier League Technical Department — Database Management Team recruitment**.

The primary focus is on demonstrating the ability to connect an application layer with a relational database and perform structured data operations programmatically.

---

## 🔐 Security Note

This repository intentionally does **not** contain database passwords, credentials, API keys, or other sensitive information.

Before running the application, configure the MySQL credentials locally.

---

## 📄 License

This project is intended for educational and recruitment purposes.
