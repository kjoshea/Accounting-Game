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

    # RECORD AN INCREASE IN INVENTORY
    def debit_inventory(self):
        self.inventory += int(input("Input increase in inventory:"))

    # RECORD AN DECREASE IN INVENTORY
    def credit_inventory(self):
        self.inventory -= int(input("Input decrease in inventory:"))


# ***** START OF GAME *****

# INITIALIZE FINANCIAL STATEMENTS WITH 10 INVENTORY
game_IS = IncomeStatement(0, 0)
game_BS = BalanceSheet(0, 10)

# GAME LOGIC
while True:
    # DISPLAY CURRENT FINANCIAL STATEMENTS
    print()
    print(game_IS.display())
    print(game_BS.display())
    print()

    # STOP THE GAME WHEN THE BALANCE SHEET HAS AT LEAST 50 EQUITY
    if game_BS.equity > 50:
        print("Congratulations, you have grown equity to {}. You win!".format(game_BS.equity))
        print("GAME OVER")
        break

    # CHOOSE A MOVE FROM THE OPTIONS
    print("These are your possible moves")
    print("-----------------------------")
    print("Press 1: Record a Sale")
    print("Press 2: Purchase Inventory")
    move = int(input("What is your move?"))

    # DETERMINE YOUR MOVE WILL DO
    if move == 1:
        print()
        print("Input the sale amount below.")
        game_IS.credit_sales()
        game_BS.debit_cash()
        print()
        print("Input the value of inventory sold.")
        game_BS.credit_inventory()
        game_IS.debit_expenses()
    elif move == 2:
        print()
        print("Input the amount of inventory to purchase.")
        game_BS.debit_inventory()
        game_BS.debit_cash()
    else:
        print("You did not select an available option.")


