# Budget App
# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment.
# These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories
#
# Push your code to GitHub, and submit the repo link

class Budget:
    foodBalance = 0
    clothingBalance = 0
    entertainmentBalance = 0

    # def __init__(self, food, clothing, entertainment):
    #     self.foodValue = food
    #     self.clothingValue = clothing
    #     self.entertainmentValue = entertainment

    def deposit(self, f, c, e):
        print("Deposited value is food: {}, clothing: {}, entertainment: {}"
              .format(f, c, e))

        self.foodBalance += f
        self.clothingBalance += c
        self.entertainmentBalance += e

        print("Current Balance is food: {}, clothing: {}, entertainment: {}"
              .format(self.foodBalance, self.clothingBalance, self.entertainmentBalance))

    def withdraw(self, f, c, e):

        if f > self.foodBalance:
            print("Error! food balance is less than the required value")
        elif c > self.clothingBalance:
            print("Error! clothing balance is less than the required value")
        elif e > self.entertainmentBalance:
            print("Error! entertainment balance is less than the required value")
        else:
            self.foodBalance -= f
            self.clothingBalance -= c
            self.entertainmentBalance -= e

            print("Current Balance is food: {}, clothing: {}, entertainment: {}"
                  .format(self.foodBalance, self.clothingBalance, self.entertainmentBalance))

    def transferBalance(self):
        transfer_code = input("""Transfer from
1: food > clothing
2: food > entertainment
3: clothing > food
4: clothing > entertainment
5: entertainment > food
6: entertainment > clothing\n """)

        if transfer_code == str(1):
            amount = int(input("Enter amount: "))
            self.foodBalance -= amount
            self.clothingBalance += amount
            print("Current Balance is food: {}, clothing: {}, entertainment: {}"
                  .format(self.foodBalance, self.clothingBalance, self.entertainmentBalance))

        elif transfer_code == str(2):
            amount = int(input("Enter amount: "))
            self.foodBalance -= amount
            self.entertainmentBalance += amount
            print("Current Balance is food: {}, clothing: {}, entertainment: {}"
                  .format(self.foodBalance, self.clothingBalance, self.entertainmentBalance))

        elif transfer_code == str(3):
            amount = int(input("Enter amount: "))
            self.clothingBalance -= amount
            self.foodBalance += amount
            print("Current Balance is food: {}, clothing: {}, entertainment: {}"
                  .format(self.foodBalance, self.clothingBalance, self.entertainmentBalance))

        elif transfer_code == str(4):
            amount = int(input("Enter amount: "))
            self.clothingBalance -= amount
            self.entertainmentBalance += amount
            print("Current Balance is food: {}, clothing: {}, entertainment: {}"
                  .format(self.foodBalance, self.clothingBalance, self.entertainmentBalance))

        elif transfer_code == str(5):
            amount = int(input("Enter amount: "))
            self.entertainmentBalance -= amount
            self.foodBalance += amount
            print("Current Balance is food: {}, clothing: {}, entertainment: {}"
                  .format(self.foodBalance, self.clothingBalance, self.entertainmentBalance))

        elif transfer_code == str(6):
            amount = int(input("Enter amount: "))
            self.entertainmentBalance -= amount
            self.clothingBalance += amount
            print("Current Balance is food: {}, clothing: {}, entertainment: {}"
                  .format(self.foodBalance, self.clothingBalance, self.entertainmentBalance))

        else:
            print("Input entered incorrect")


# budget object
firstBudget = Budget()
print(firstBudget.deposit(700, 200, 100))
print(firstBudget.withdraw(200, 50, 10))
print(firstBudget.transferBalance())