# Improve on your ATM mockup from last course to include the following:
# 1. Use functions
# 2. Include register, and login
# 3. Generate Account Number
# 4. Any other improvement you can think of (extra point)
import datetime, random
# 1. The user should see the current date and time after they log in
# 2. When the user selects option 1, they should be presented with the following:
# - How much would you like to withdraw (receive input from the user), output "take your cash"
# 3. When the user selects option 2, present them with the following options:
# - How much would you like to deposit? (receive input from the user), output current balance.
# 4. When the user selects complaint, present them with the following options:
# - What issue will you like to report? (Receive input from the user), output "Thank you for contacting us"


# functions
def login_user(account_number, user_pin):

    if account_number in registered_users and registered_users[account_number][2] == user_pin:
        print("Welcome {}".format(registered_users[account_number][0]))
    
        option = input("""Please choose an option
1 - withdraw | 2 - deposit | 3 - complain \n """)

        if option == str(1) or option == "withdraw":
            withdraw = int(input("How much would you like to withdraw \n"))

            if withdraw > registered_users[account_number][1]:
                print("Account Balance is low")
            else:
                registered_users[account_number][1] -= int(withdraw)
                print("Please take your cash")

        elif option == str(2) or option == "deposit":
            deposit = int(input("How much would you like to deposit? \n"))
            registered_users[account_number][1] += int(deposit)
            print("Current balance is: {}".format(registered_users[account_number][1]))

        elif option == str(3) or option == "complain":
            complain = input("What issue will you like to report? \n")
            print("Thank you for contacting us")

        else:
            print("input entered not a command")

    else:
        print("Account does not exist or user pin incorrect. Please check and try again")


def register_user(name, account_pin):

    # generating account number
    generate_account_number(name, account_pin)
    # print("Congratulations! your account has been created and your account number is {} ".format(account_number))


# generating account number
def generate_account_number(name, account_pin):
    # generating account number
    ramdomlist = random.sample(range(0, 10), 10)
    strings = [str(integer) for integer in ramdomlist]
    a_string = "".join(strings)
    account_number = int(a_string)

    if account_number in registered_users:
        # recursive call to create account number if account number already exist
        generate_account_number()

    else:
        registered_users[account_number] = []
        registered_users[account_number].extend([name, total_balance, account_pin])
        print("Congratulations! your account has been created and your account number is {} ".format(account_number))


total_balance = 0

#should use dictionary (account number: [name, balance, pin])
registered_users = {
    1234567890: ["ali", 500, 1234],
    9876543210: ["musa", 300, 4321],
    1357902468: ["bello", 100, 1234]
}   

# registered_users = [1234567890]

while True:
    today_date = datetime.datetime.now()
    print("Today's Date is {} and the time is {}".format(today_date.strftime("%a %d/%b/%Y"),
    today_date.strftime("%I:%M%p")))


    register_login = input("""Hello! What would you like to do?
    1 - Register
    2 - Login\n """)

    if register_login == str(1):
        name = input("Enter name: ")
        account_pin = int(input("Enter account pin: "))

        register_user(name, account_pin)
        # print("Register")

    elif register_login == str(2):
        user_account_number = int(input("Enter account number: "))
        user_pin = int(input("Enter user pin: "))

        login_user(user_account_number, user_pin)         

    else:
        print("Input not recognise")





