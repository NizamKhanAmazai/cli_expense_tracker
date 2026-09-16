# """All calculation of expenses"""

def get_monthly_stats(data, month, year):
    expense = 0

    for e in data:
        expMonth = e['date'].split('-')[1]
        expYear = e['date'].split('-')[0]

        if expMonth == month and expYear == year: 
            expense += int(e['amount']) 
 
    print(f"\t| {'Expense':<15} | {'Month':<6} | {'Year':<10} |")
    print('-'*55)  
    print(f"\t| {expense:<15,} | {month:<6} | {year:<10} |")


def show_total_expense(data):
    """calculating total expense"""
    expense = 0
    
    for e in data:  
        expense += int(e['amount']) 
     
    print('-'*50)
    print(f"\t| {'Expense:':<20} {expense}|")
    print('-'*50)


def show_average_expenses(data):
    """showing average expense"""
    expense = 0 
    for e in data:  
        expense += int(e['amount'])  
 
    expense = expense/len(data)

    print('-'*50)
    print(f"\t| {'Average expenses:':<20} {round(expense,2):<20} |")
    print('-'*50)


def expenses_by_category(data):
    """show expense and it category"""
    expense = {}

    for e in data:
        if e['category'] in expense.keys():
            exp = expense[e['category']]
            expense[e['category']] = exp+float(e['amount'])
        else:
            expense[e['category']] = e['amount'] 

    print(f"\t| {'Category':<20} | {'Amount':<10} |")
    print('-'*55)
    for k,v in expense.items():
        print(f"\t| {k:<20} : {v:<10} |")


def highest_expense(data):
    """show highest expense""" 
    amounts = []

    for e in data:
        amounts.append(e['amount'])
 
    print('-'*50)
    print(f"\t| {'Max amount:':<20} {max(amounts)} |")
    print('-'*50)


def count_expense(data):
    print('-'*50)
    print(f"\t| {'Number of expenses:':<20} {len(data)} |")
    print('-'*50)
