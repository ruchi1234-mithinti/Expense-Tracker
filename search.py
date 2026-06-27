from database import get_connection
from expense import CATEGORIES, display_categories

def search_expense():
    print("\n--- Search Expenses ---")
    print("1. Search by Category")
    print("2. Search by Date")
    choice = input("Choose search criteria: ").strip()

    conn = get_connection()
    cursor = conn.cursor()

    if choice == '1':
        display_categories()
        try:
            cat_choice = int(input("Select category number: "))
            if 1 <= cat_choice <= len(CATEGORIES):
                category = CATEGORIES[cat_choice - 1]
            else:
                print("Invalid choice.")
                conn.close()
                return
        except ValueError:
            print("Invalid input.")
            conn.close()
            return
        
        cursor.execute("SELECT id, amount, category, description, date FROM expenses WHERE category = ? ORDER BY date DESC", (category,))
        records = cursor.fetchall()
        
    elif choice == '2':
        date_str = input("Enter specific date (YYYY-MM-DD) or month (YYYY-MM): ").strip()
        cursor.execute("SELECT id, amount, category, description, date FROM expenses WHERE date LIKE ? ORDER BY date DESC", (f"{date_str}%",))
        records = cursor.fetchall()
    else:
        print("Invalid option.")
        conn.close()
        return

    conn.close()

    if not records:
        print("No matching expenses found.")
        return

    print(f"\n{'ID':<5} | {'Date':<12} | {'Category':<15} | {'Amount (₹)':<12} | {'Description'}")
    print("-" * 70)
    for row in records:
        print(f"{row[0]:<5} | {row[4]:<12} | {row[2]:<15} | {row[1]:<12.2f} | {row[3]}")