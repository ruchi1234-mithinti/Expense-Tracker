# 💰 Expense Tracker System

A Python-based **Expense Tracker System** built using **SQLite** that helps users manage their daily income and expenses through a simple menu-driven command-line interface. The application stores transaction records, categorizes expenses, generates financial summaries, and allows users to search and manage their financial data efficiently.

---

## 📌 Features

### 💵 Income Management

* Add Income
* View Income History

### 💸 Expense Management

* Add Expense
* View Expense History
* Delete Expense

### 🔍 Search Expenses

* Search by Category
* Search by Date

### 📊 Reports

* Category-wise Expense Report
* Monthly Expense Report
* Financial Summary
* Remaining Balance Calculation
* Highest Spending Category

### 💾 Database

* SQLite Database Integration
* Automatic Table Creation
* Persistent Data Storage

---

## 🛠️ Technologies Used

* Python 3
* SQLite (sqlite3)
* VS Code
* Git & GitHub

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
├── .gitignore
└── screenshots/
```

---

## 🗄️ Database Tables

### Income

| Column | Type                              |
| ------ | --------------------------------- |
| id     | INTEGER PRIMARY KEY AUTOINCREMENT |
| amount | REAL                              |
| source | TEXT                              |
| date   | TEXT                              |

### Expenses

| Column      | Type                              |
| ----------- | --------------------------------- |
| id          | INTEGER PRIMARY KEY AUTOINCREMENT |
| amount      | REAL                              |
| category    | TEXT                              |
| description | TEXT                              |
| date        | TEXT                              |

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/ruchi1234-mithinti/Expense-Tracker.git
```

2. Navigate to the project folder

```bash
cd Expense-Tracker
```

3. Run the application

```bash
python main.py
```

---

## 📋 Menu

```
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

## 📷 Screenshots

Add screenshots of the following:

* Home Menu
* Add Income
* Add Expense
* View Expenses
* Search Expense
* Category Report
* Monthly Report
* Financial Summary

---

## 🎯 Learning Outcomes

This project demonstrates:

* Python Programming
* SQLite Database Operations
* CRUD Operations
* Menu-Driven Applications
* Modular Programming
* Functions
* SQL Queries
* Data Management
* Basic Financial Record Management

---

## 🚀 Future Enhancements

* User Authentication
* Budget Planning
* Expense Limit Alerts
* Export Reports to CSV/PDF
* Graphical Reports
* GUI using Tkinter
* Data Backup & Restore

---

## 👩‍💻 Author

**Ruchitha Mithinti**

GitHub: https://github.com/ruchi1234-mithinti
