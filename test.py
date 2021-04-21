# print("Hello py")
# name = input("what is your name?")
# print("My name is {}".format(name))


import random
# rand_list = []
# for i in range(0,10):
#     n = random.randint(0,9)
#     rand_list.append(n)
# print(rand_list)

# ramdomlist = random.sample(range(0, 10), 10)
# strings = [str(integer) for integer in ramdomlist]
# a_string = "".join(strings)
# an_integer = int(a_string)
# print(an_integer)


# registered_users = {
#     1234567890: ["ali", 500, 1234],
#     9876543210: ["musa", 300, 4321],
#     1234567890: ["bello", 100, 1234]
# } 

# print(registered_users[1234567890][0])

# registered_users[3333] = []
# registered_users[3333].extend(["ahmed", 0, 1234])
# # registered_users[3333][1] = 0
# # registered_users[3333][2] = 1234

# print(registered_users[3333])


# def tri_recursion(k):
#     if k > 0:
#         result = k + tri_recursion(k - 1)

#     else:
#         result = 0
#     return result

# recursive_func = tri_recursion(6)
# print(recursive_func)

account_numbers = [1234567890, 9876543210]

# def gen_acct_num():
#     # generating account number
#     ramdomlist = random.sample(range(0, 10), 10)
#     strings = [str(integer) for integer in ramdomlist]
#     a_string = "".join(strings)
#     account_number = int(a_string)

#     if account_number in account_numbers:
#         gen_acct_num()

#     else:
#         account_numbers.append(account_number)

#     # registered_users[account_number] = []
#     # registered_users[account_number].extend([name, total_balance, account_pin])

# gen_acct_num()
# print(account_numbers)