# 💰 Expense Tracker System

A Python-based Expense Tracker System built using SQLite that helps users manage their daily income and expenses through a simple menu-driven command-line interface. The application stores transaction records, categorizes expenses, generates financial reports, and maintains transaction history.

---

## 📌 Features

### 💵 Income Management
- Add Income
- View Income History

### 💸 Expense Management
- Add Expense
- View Expense History
- Delete Expense

### 🔍 Search Transactions
- Search Expenses by Category
- Search Expenses by Date

### 📊 Reports
- Category-wise Expense Report
- Monthly Expense Report
- Financial Summary
- Remaining Balance
- Highest Spending Category

### 💾 Database
- SQLite Database Integration
- Automatic Table Creation
- Persistent Data Storage

---

## 🛠️ Technologies Used

- Python 3
- SQLite (sqlite3)
- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```
Expense-Tracker/
│
├── main.py
├── database.py
├── income.py
├── expense.py
├── report.py
├── search.py
├── README.md
└── .gitignore
```

---

## 🗄️ Database Schema

### Income Table

| Column | Type |
|---------|------|
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| amount | REAL |
| source | TEXT |
| date | TEXT |

### Expense Table

| Column | Type |
|---------|------|
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| amount | REAL |
| category | TEXT |
| description | TEXT |
| date | TEXT |

---

## ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/ruchi1234-mithinti/Expense-Tracker.git
```

Go to the project folder

```bash
cd Expense-Tracker
```

Run the project

```bash
python main.py
```

---

## 📋 Menu

```
========== Expense Tracker ==========

1. Add Income
2. View Income
3. Add Expense
4. View Expenses
5. Delete Expense
6. Search Expense
7. Category Report
8. Monthly Report
9. Financial Summary
0. Exit
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python Programming
- SQLite Database Operations
- CRUD Operations
- SQL Queries
- Menu-Driven Applications
- Modular Programming
- Functions
- Database Connectivity
- Financial Data Management

---

## 🚀 Future Enhancements

- User Authentication
- Budget Planning
- Expense Limit Alerts
- Export Reports to CSV
- PDF Report Generation
- Graphical Reports
- GUI using Tkinter
- Data Backup and Restore
