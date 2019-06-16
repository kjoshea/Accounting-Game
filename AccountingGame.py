# CREATE THE INCOME STATEMENT CLASS
class IncomeStatement:
    def __init__(self, sales, expenses):
        self.sales = sales
        self.expenses = expenses
        self.income = sales - expenses

    # DISPLAY THE CURRENT INCOME STATEMENT
    def display(self):
        self.income = self.sales - self.expenses
        print("Sales: {} Expenses: {} || Income: {}".format(self.sales, self.expenses, self.income))

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
        print("Cash: {} Inventory: {} || Equity: {}".format(self.cash, self.inventory, self.equity))

    # RECORD AN INCREASE IN CASH
    def debit_cash(self):
        self.cash += int(input("Input increase in cash:"))

    # RECORD A DECREASE IN CASH
    def credit_cash(self):
        cash_to_decrease = int(input("Input decrease in cash:"))
        if cash_to_decrease <= game_BS.cash:
            self.cash -= cash_to_decrease
        else:
            print("Amount entered too high. You have {} cash available".format(game_BS.cash))
            game_BS.credit_cash()

    # RECORD AN INCREASE IN INVENTORY
    def debit_inventory(self):
        self.inventory += int(input("Input increase in inventory:"))

    # RECORD AN DECREASE IN INVENTORY
    def credit_inventory(self):
        inventory_to_decrease = int(input("Input decrease in inventory:"))
        if inventory_to_decrease <= game_BS.inventory:
            self.inventory -= inventory_to_decrease
        else:
            print("Amount entered too high. You have {} inventory available.".format(game_BS.inventory))
            game_BS.credit_inventory()


# ***** START OF GAME *****

# INITIALIZE FINANCIAL STATEMENTS WITH 10 INVENTORY
game_IS = IncomeStatement(0, 0)
game_BS = BalanceSheet(0, 10)

# INITIALIZE MOVE COUNTER
move_counter = 0

# ANNOUNCE GAME START
print("GAME START")
print()
print("These are your starting financial statements.")

# GAME LOGIC
while True:
    # DISPLAY CURRENT FINANCIAL STATEMENTS
    print()
    game_IS.display()
    game_BS.display()
    print()

    # STOP THE GAME WHEN THE BALANCE SHEET HAS AT LEAST 50 EQUITY
    if game_BS.equity > 50:
        print("Congratulations, you have grown equity to {} in {} {}. You win!".format(game_BS.equity,move_counter,
              "move" if move_counter == 1 else "moves"))
        print("GAME OVER")
        break

    # CHOOSE A MOVE FROM THE OPTIONS
    print("These are your possible moves")
    print("-----------------------------")
    print("Press 1: Record a Sale")
    print("Press 2: Purchase Inventory")
    move = int(input("What is your move? "))

    # DETERMINE YOUR MOVE WILL DO
    if move == 1:
        print("-----------------------------")
        print("You have {} inventory available".format(game_BS.inventory))
        print()
        print("Input the value of inventory sold.")
        game_BS.credit_inventory()
        game_IS.debit_expenses()
        print()
        print("Input the sale amount below.")
        game_IS.credit_sales()
        game_BS.debit_cash()

    elif move == 2:
        print()
        print("Input the amount of inventory to purchase.")
        game_BS.credit_cash()
        game_BS.debit_inventory()

    else:
        print("You did not select an available option.")

    # INCREASE MOVE COUNTER
    move_counter += 1

