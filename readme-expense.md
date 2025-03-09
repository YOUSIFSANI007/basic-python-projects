# Expense Tracker

A Python-based expense tracking application that helps you monitor and analyze your spending.

## Features

- Add expenses with categories and descriptions
- View monthly expense summaries
- Generate custom date range reports
- Analyze spending by category
- Persistent data storage using JSON
- Input validation and error handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/expense-tracker
cd expense-tracker
```

2. No additional packages required - uses only Python standard library!

## Usage

Run the program:
```bash
python expense_tracker.py
```

### Main Menu Options

1. **Add Expense**
   - Enter amount
   - Select category
   - Add description

2. **View Monthly Summary**
   - See total expenses for a specific month
   - View breakdown by category
   - List all expenses for the month

3. **View Category Breakdown**
   - See total spending by category
   - View percentage distribution

4. **Generate Custom Report**
   - Select date range
   - View all expenses in period
   - See total for period

5. **View All Categories**
   - List available expense categories

### Available Categories

- Food
- Transportation
- Housing
- Utilities
- Entertainment
- Shopping
- Healthcare
- Other

## Data Storage

- Expenses are stored in `expenses.json`
- Format:
```json
[
    {
        "date": "2024-02-21",
        "amount": 50.00,
        "category": "Food",
        "description": "Grocery shopping"
    }
]
```

## Tips for Use

1. Enter dates in YYYY-MM-DD format
2. Amounts are rounded to 2 decimal places
3. Categories must be selected from the predefined list
4. Descriptions help track expense details
5. Regular backups of expenses.json recommended

## Contributing

To enhance the expense tracker:

1. Add new features:
   - Budget tracking
   - Data visualization
   - Export to spreadsheet
   - Multiple currencies
   - Recurring expenses

2. Improve existing features:
   - Additional report types
   - More category options
   - Advanced analytics

## License

MIT License
