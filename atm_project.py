import datetime
# 1. The user should see the current date and time after they log in
# 2. When the user selects option 1, they should be presented with the following:
# - How much would you like to withdraw (receive input from the user), output "take your cash"
# 3. When the user selects option 2, present them with the following options:
# - How much would you like to deposit? (receive input from the user), output current balance.
# 4. When the user selects complaint, present them with the following options:
# - What issue will you like to report? (Receive input from the user), output "Thank you for contacting us"


today_date = datetime.datetime.now()
print("Today's Date is {} and the time is {}".format(today_date.strftime("%a %d/%b/%Y"),
today_date.strftime("%I:%M%p")))

total_balance = 0

option = input("""Please choose an option
1 - withdraw | 2 - deposit | 3 - complain \n """)

if option == str(1) or option == "withdraw":
    withdraw = input("How much would you like to withdraw \n")
    print("Please take your cash")

elif option == str(2) or option == "deposit":
    deposit = input("How much would you like to deposit? \n")
    total_balance += int(deposit)
    print("Current balance: {}".format(total_balance))

elif option == str(3) or option == "complain":
    complain = input("What issue will you like to report? \n")
    print("Thank you for contacting us")

else:
    print("input entered not a command")

