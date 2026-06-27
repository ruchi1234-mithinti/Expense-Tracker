import sys
from database import initialize_db
import income
import expense
import search
import report

def main_menu():
    print("\n========== Expense Tracker ==========")
    print("1. Add Income")
    print("2. View Income")
    print("3. Add Expense")
    print("4. View Expenses")
    print("5. Delete Expense")
    print("6. Search Expense")
    print("7. Category Report")
    print("8. Monthly Report")
    print("9. Financial Summary")
    print("0. Exit")
    print("=====================================")

def main():
    # Setup step to ensure architecture parameters are ready
    initialize_db()
    
    while True:
        main_menu()
        choice = input("Select an option (0-9): ").strip()
        
        if choice == '1':
            income.add_income()
        elif choice == '2':
            income.view_income()
        elif choice == '3':
            expense.add_expense()
        elif choice == '4':
            expense.view_expenses()
        elif choice == '5':
            expense.delete_expense()
        elif choice == '6':
            search.search_expense()
        elif choice == '7':
            report.category_report()
        elif choice == '8':
            report.monthly_report()
        elif choice == '9':
            report.financial_summary()
        elif choice == '0':
            print("\nThank you for using Expense Tracker System. Goodbye!")
            sys.exit()
        else:
            print("Invalid input! Please input a value between 0 and 9.")

if __name__ == "__main__":
    main()