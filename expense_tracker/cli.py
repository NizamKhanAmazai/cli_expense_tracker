import argparse
from expense_tracker import ExpenseService, start
import shlex 
from tests.run_test import run_test

def start_cmd():
    parser = argparse.ArgumentParser(
        prog='expense',
        description="Track your expense from the command line"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    #1. expense add 500 food "lunch"
    add_parser = subparsers.add_parser("add", help="Add a new expense ------------------ 🟢 add 400 Food Party with friends")
    add_parser.add_argument("amount", type=float)
    add_parser.add_argument("category")
    add_parser.add_argument("description", nargs="*", default="")

    #2. Expense list
    list_parser = subparsers.add_parser("list", help="List all expenses by category ------ 🟢 list")
    list_parser.add_argument("--category", help="Filter by category")

    #3. delete expense
    del_parser = subparsers.add_parser("delete", help="Delete an expense by id ------------ 🟢 delete 5")
    del_parser.add_argument("id", type=int)

    #4. Search expense
    search_parser = subparsers.add_parser("search", help="Search expense by keyword ---------- 🟢 search 'id/amount/category/desc'")
    search_parser.add_argument("keyword")

    #5. Categories
    category_parser = subparsers.add_parser('categories', help="Show all categories ---------------- 🟢 categories")
    category_parser.add_argument('--categories', help='Show all categories')

    #6. Total Expenses
    total_expenses = subparsers.add_parser('total', help='Show total expenses ---------------- 🟢 total')
    total_expenses.add_argument('--total expenses', help='Show total expenses')

    #7. Average Expense
    avg_expense = subparsers.add_parser('average', help="Show average expese ---------------- 🟢 average")
    avg_expense.add_argument('--average expense', help="Show average expese")

    #8. Expenses by category
    exp_by_categ = subparsers.add_parser('expense_by_category', help="show expense by category ----------- 🟢 expense_by_category ")
    exp_by_categ.add_argument('--category name')

    #9. Monthly Spending 
    m_stats = subparsers.add_parser("m-stats", help="Show mounthly statistics ----------- 🟢 m-stats month year")
    m_stats.add_argument('month', type=str)
    m_stats.add_argument('year', type=str)

    #10. Highest Expense
    high_exp = subparsers.add_parser('max', help="Show Highest expense --------------- 🟢 max")
    high_exp.add_argument('--high', help='Show highest expense')

    #11. Number of expenses
    count_exp = subparsers.add_parser('count', help="Show number of expenses ------------ 🟢 count")
    count_exp.add_argument('--count', help='Show number of expenses')

    #12. Test the app
    test_app = subparsers.add_parser('test', help='Test application ------------------- 🟢 test')
    test_app.add_argument('--test', help="Test application")

    #13. Save the data as Json
    save_to_json = subparsers.add_parser('save_to_json', help="Save the data in json -------------- 🟢 save_to_json 'fileName' ")
    save_to_json.add_argument('fileName', type=str)

    # args = parser.parse_args()
    services = ExpenseService()
 
    start()
    print("\n\nExpense tracker CLI initialized. Type 'exit' or 'quit' to close." )

    # #show help to user
    # parser.print_help() 

    while True:
        try:
            #1. Get input from the user
            userInput = input("Expense> ").strip()

            #2. Check for exit conditions
            if userInput.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break

            if not userInput:
                continue

            #Safely split the string into list of arguments (respecting quotes)
            args_list = shlex.split(userInput)

            args = parser.parse_args(args_list)

            #Route the cammads
            if args.command == "add":
                desc = " ".join(args.description) if args.description else ""
                services.add_expense(args.amount, args.category, desc)

            elif args.command == "list":
                services.list_expenses(args.category) 

            elif args.command == "delete":
                services.delete_expense(args.id) 

            elif args.command == "search":
                services.search_expenses(args.keyword)

            elif args.command == 'categories':
                services.show_all_categories()

            elif args.command == 'm-stats':
                services.monthly_statistics(args.month, args.year)

            elif args.command == 'total':
                services.total_expenses()
            
            elif args.command == 'average':
                services.average_expense()

            elif args.command == 'expense_by_category':
                services.expenses_by_category()
            
            elif args.command == 'max':
                services.highest_expense()
            
            elif args.command == 'count':
                services.count_expenses()

            elif args.command == 'test':
                run_test()

            elif args.command == 'save_to_json':
                services.save_to_json(args.fileName)
 

        except SystemExit:
            # Catch argparse's default behavior on error or '--help'
            # So it doesn't crash the whole loop.
            continue

        # except Exception as e:
        #     print(f"Error: {e}") 