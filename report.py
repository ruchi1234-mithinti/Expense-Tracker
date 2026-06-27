from database import get_connection

def category_report():
    print("\n--- Category-wise Expense Summary ---")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY SUM(amount) DESC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No dynamic data available.")
        return

    print(f"{'Category':<18} | {'Total Spent (₹)':<15}")
    print("-" * 36)
    for row in rows:
        print(f"{row[0]:<18} | {row[1]:<15.2f}")

def monthly_report():
    print("\n--- Monthly Expense Report ---")
    month_str = input("Enter month (YYYY-MM) [e.g., 2026-06]: ").strip()
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses WHERE date LIKE ? GROUP BY category", (f"{month_str}%",))
    rows = cursor.fetchall()
    
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE date LIKE ?", (f"{month_str}%",))
    total_month_expense = cursor.fetchone()[0] or 0.0
    conn.close()

    if not rows:
        print(f"No records found for the period: {month_str}")
        return

    print(f"\nBreakdown for {month_str}:")
    print(f"{'Category':<18} | {'Spent (₹)':<15}")
    print("-" * 36)
    for row in rows:
        print(f"{row[0]:<18} | {row[1]:<15.2f}")
    print("-" * 36)
    print(f"Total Monthly Expenses: ₹{total_month_expense:.2f}")

def financial_summary():
    print("\n================ Financial Summary ================")
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM income")
    total_income = cursor.fetchone()[0] or 0.0
    
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_expenses = cursor.fetchone()[0] or 0.0
    
    cursor.execute("SELECT category, SUM(amount) as total FROM expenses GROUP BY category ORDER BY total DESC LIMIT 1")
    highest_spending_row = cursor.fetchone()
    
    conn.close()

    remaining_balance = total_income - total_expenses

    print(f"Total Income      : ₹{total_income:,.2f}")
    print(f"Total Expenses    : ₹{total_expenses:,.2f}")
    print(f"Remaining Balance : ₹{remaining_balance:,.2f}")
    print("-" * 47)
    
    if highest_spending_row:
        print(f"Highest Spending Category: {highest_spending_row[0]} (₹{highest_spending_row[1]:,.2f})")
    else:
        print("Highest Spending Category: N/A")
    print("===================================================")