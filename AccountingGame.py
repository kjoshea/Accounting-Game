
class IncomeStatement:
    def __init__(self, sales, expenses):
        self.sales = sales
        self.expenses = expenses
        self.income = sales - expenses

    def display(self):
        self.income = self.sales - self.expenses
        return "Sales: {} Expenses: {} || Income: {}".format(self.sales, self.expenses, self.income)

    def credit_sales(self):
        self.sales = self.sales + int(input("Input sale amount:"))

    def debit_expenses(self):
        self.expenses = self.expenses + int(input("Input expense amount:"))


class BalanceSheet:
    def __init__(self, cash, inventory):
        self.cash = cash
        self.inventory = inventory
        self.equity = cash + inventory

    def display(self):
        self.equity = self.cash + self.inventory
        return "Cash: {} Inventory: {} || Equity: {}".format(self.cash, self.inventory, self.equity)


example_IS = IncomeStatement(0, 0)
example_BS = BalanceSheet(0, 0)

print(example_IS.display())
print(example_BS.display())

