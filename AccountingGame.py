# CREATE THE INCOME STATEMENT CLASS
class IncomeStatement:
    def __init__(self, sales, expenses):
        self.sales = sales
        self.expenses = expenses
        self.income = sales - expenses

    # DISPLAY THE CURRENT INCOME STATEMENT
    def display(self):
        self.income = self.sales - self.expenses
        return "Sales: {} Expenses: {} || Income: {}".format(self.sales, self.expenses, self.income)

    # RECORD A SALE
    def credit_sales(self):
        self.sales += int(input("Input sale amount:"))

    # RECORD AN EXPENSE
    def debit_expenses(self):
        self.expenses += int(input("Input expense amount:"))


# CREATE THE BALANCE SHEET CLASS
class BalanceSheet:
    def __init__(self, cash, inventory):
        self.cash = cash
        self.inventory = inventory
        self.equity = cash + inventory

    # DISPLAY THE CURRENT BALANCE SHEET
    def display(self):
        self.equity = self.cash + self.inventory
        return "Cash: {} Inventory: {} || Equity: {}".format(self.cash, self.inventory, self.equity)

    # RECORD AN INCREASE (DECREASE) IN CASH
    def debit_cash(self):
        self.cash += int(input("Input increase (decrease) in cash:"))

    # RECORD AN INCREASE (DECREASE) INVENTORY
    def debit_inventory(self):
        self.inventory += int(input("Input increase (decrease) in inventory:"))


# PRINT INITIAL FINANCIAL STATEMENTS
example_IS = IncomeStatement(0, 0)
example_BS = BalanceSheet(0, 0)

print(example_IS.display())
print(example_BS.display())

# EXAMPLE OF A SALE
example_IS.credit_sales()
print(example_IS.display())
example_BS.debit_cash()
print(example_BS.display())

# EXAMPLE OF AN EXPENSE RECORDING
example_IS.debit_expenses()
print(example_IS.display())
example_BS.debit_inventory()
print(example_BS.display())

