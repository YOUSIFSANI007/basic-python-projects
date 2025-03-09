import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import calendar

class ExpenseTracker:
    def __init__(self, filename: str = "expenses.json"):
        self.filename = filename
        self.expenses: List[Dict] = []
        self.categories = [
            "Food", "Transportation", "Housing", "Utilities",
            "Entertainment", "Shopping", "Healthcare", "Other"
        ]
        self.load_expenses()

    def load_expenses(self) -> None:
        """Load expenses from JSON file"""
        try:
            if Path(self.filename).exists():
                with open(self.filename, 'r') as f:
                    self.expenses = json.load(f)
        except json.JSONDecodeError:
            print("Error reading expense file. Starting with empty expense list.")
            self.expenses = []

    def save_expenses(self) -> None:
        """Save expenses to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, amount: float, category: str, description: str) -> None:
        """Add a new expense"""
        if category not in self.categories:
            raise ValueError(f"Invalid category. Choose from: {', '.join(self.categories)}")

        expense = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()

    def get_monthly_summary(self, year: int, month: int) -> Dict:
        """Generate monthly expense summary"""
        monthly_expenses = [
            expense for expense in self.expenses
            if datetime.strptime(expense['date'], '%Y-%m-%d').year == year
            and datetime.strptime(expense['date'], '%Y-%m-%d').month == month
        ]

        summary = {
            'total': sum(expense['amount'] for expense in monthly_expenses),
            'by_category': {},
            'expenses': monthly_expenses
        }

        # Calculate totals by category
        for category in self.categories:
            category_total = sum(
                expense['amount'] for expense in monthly_expenses
                if expense['category'] == category
            )
            if category_total > 0:
                summary['by_category'][category] = category_total

        return summary

    def get_expense_report(self, start_date: str, end_date: str) -> List[Dict]:
        """Generate expense report for date range"""
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')

        return [
            expense for expense in self.expenses
            if start <= datetime.strptime(expense['date'], '%Y-%m-%d') <= end
        ]

    def get_category_breakdown(self) -> Dict[str, float]:
        """Get total expenses by category"""
        breakdown = {category: 0.0 for category in self.categories}
        for expense in self.expenses:
            breakdown[expense['category']] += expense['amount']
        return {k: v for k, v in breakdown.items() if v > 0}

def print_menu() -> None:
    """Display main menu"""
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Monthly Summary")
    print("3. View Category Breakdown")
    print("4. Generate Custom Report")
    print("5. View All Categories")
    print("6. Exit")

def get_valid_date(prompt: str) -> str:
    """Get and validate date input"""
    while True:
        try:
            date_str = input(prompt + " (YYYY-MM-DD): ")
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

def get_valid_amount() -> float:
    """Get and validate amount input"""
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than 0")
                continue
            return round(amount, 2)
        except ValueError:
            print("Please enter a valid number")

def main():
    tracker = ExpenseTracker()

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            # Add expense
            print("\n=== Add New Expense ===")
            amount = get_valid_amount()
            
            print("\nAvailable categories:")
            for i, category in enumerate(tracker.categories, 1):
                print(f"{i}. {category}")
            
            while True:
                try:
                    cat_num = int(input("\nSelect category number: "))
                    category = tracker.categories[cat_num - 1]
                    break
                except (ValueError, IndexError):
                    print("Please enter a valid category number")
            
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
            print("Expense added successfully!")

        elif choice == '2':
            # Monthly summary
            try:
                year = int(input("Enter year (YYYY): "))
                month = int(input("Enter month (1-12): "))
                summary = tracker.get_monthly_summary(year, month)
                
                print(f"\n=== Summary for {calendar.month_name[month]} {year} ===")
                print(f"Total expenses: ${summary['total']:.2f}")
                
                print("\nBreakdown by category:")
                for category, amount in summary['by_category'].items():
                    print(f"{category}: ${amount:.2f}")
                
                print("\nDetailed expenses:")
                for expense in summary['expenses']:
                    print(f"{expense['date']} - {expense['category']}: "
                          f"${expense['amount']:.2f} ({expense['description']})")
                          
            except ValueError:
                print("Please enter valid year and month")

        elif choice == '3':
            # Category breakdown
            breakdown = tracker.get_category_breakdown()
            total = sum(breakdown.values())
            
            print("\n=== Category Breakdown ===")
            for category, amount in breakdown.items():
                percentage = (amount / total * 100) if total > 0 else 0
                print(f"{category}: ${amount:.2f} ({percentage:.1f}%)")

        elif choice == '4':
            # Custom report
            print("\n=== Generate Custom Report ===")
            start_date = get_valid_date("Enter start date")
            end_date = get_valid_date("Enter end date")
            
            report = tracker.get_expense_report(start_date, end_date)
            total = sum(expense['amount'] for expense in report)
            
            print(f"\nExpenses from {start_date} to {end_date}")
            print(f"Total: ${total:.2f}")
            
            for expense in sorted(report, key=lambda x: x['date']):
                print(f"{expense['date']} - {expense['category']}: "
                      f"${expense['amount']:.2f} ({expense['description']})")

        elif choice == '5':
            # View categories
            print("\n=== Available Categories ===")
            for category in tracker.categories:
                print(category)

        elif choice == '6':
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
