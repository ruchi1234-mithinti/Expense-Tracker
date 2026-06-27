from database import get_connection
from datetime import datetime

def add_income():
    print("\n--- Add Income ---")
    try:
        amount = float(input("Enter income amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount entered.")
        return

    source = input("Enter source of income: ").strip()
    if not source:
        print("Source cannot be empty.")
        return

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
        "INSERT INTO income (amount, source, date) VALUES (?, ?, ?)",
        (amount, source, date_str)
    )
    conn.commit()
    conn.close()
    print(f"✔️ Income of ₹{amount:.2f} from '{source}' added successfully!")

def view_income():
    print("\n--- Income History ---")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, amount, source, date FROM income ORDER BY date DESC")
    records = cursor.fetchall()
    conn.close()

    if not records:
        print("No income records found.")
        return

    print(f"{'ID':<5} | {'Date':<12} | {'Source':<20} | {'Amount (₹)':<12}")
    print("-" * 55)
    for row in records:
        print(f"{row[0]:<5} | {row[3]:<12} | {row[2]:<20} | {row[1]:<12.2f}")