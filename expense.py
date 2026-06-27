from database import get_connection
from datetime import datetime

CATEGORIES = [
    "Food", "Transport", "Shopping", "Bills", 
    "Entertainment", "Health", "Education", "Other"
]

def display_categories():
    print("Available Categories:")
    for idx, category in enumerate(CATEGORIES, 1):
        print(f"  {idx}. {category}")

def add_expense():
    print("\n--- Add Expense ---")
    try:
        amount = float(input("Enter expense amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount entered.")
        return

    display_categories()
    try:
        cat_choice = int(input("Select category number: "))
        if 1 <= cat_choice <= len(CATEGORIES):
            category = CATEGORIES[cat_choice - 1]
        else:
            print("Invalid choice. Defaulting to 'Other'.")
            category = "Other"
    except ValueError:
        print("Invalid input. Defaulting to 'Other'.")
        category = "Other"

    description = input("Enter brief description: ").strip()
    
    date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Using today's date instead.")
            date_str = datetime.today().strftime('%Y-%m-%d')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
        (amount, category, description, date_str)
    )
    conn.commit()
    conn.close()
    print(f"✔️ Expense of ₹{amount:.2f} under '{category}' added successfully!")

def view_expenses():
    print("\n--- Expense History ---")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, amount, category, description, date FROM expenses ORDER BY date DESC")
    records = cursor.fetchall()
    conn.close()

    if not records:
        print("No expense records found.")
        return

    print(f"{'ID':<5} | {'Date':<12} | {'Category':<15} | {'Amount (₹)':<12} | {'Description'}")
    print("-" * 70)
    for row in records:
        print(f"{row[0]:<5} | {row[4]:<12} | {row[2]:<15} | {row[1]:<12.2f} | {row[3]}")

def delete_expense():
    print("\n--- Delete Expense ---")
    view_expenses()
    try:
        expense_id = int(input("\nEnter the ID of the expense to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM expenses WHERE id = ?", (expense_id,))
    if not cursor.fetchone():
        print("Expense ID not found.")
        conn.close()
        return

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    print(f"❌ Expense ID {expense_id} deleted successfully.")