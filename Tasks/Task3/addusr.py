# # adding New user and checking if user already exists.
# import codecs
# import getpass
# def adduser(data_file):
#
#     with open(data_file, "rt") as data:
#         info = data.readlines()
#     username = input("Enter your username:")
#     realname = input("Enter your real name:")
#     # password = getpass.getpass("Enter your password: ")
#     password = input("Enter your password: ")
#     encrypted_password = codecs.encode(password, "rot_13")
#     for line in info:
#         existing_user = line.split(":")[0]
#         if username == existing_user:
#             print("User already exists.")
#             return
#     with open(data_file, 'a') as file:
#         file.writelines(f'{username}:{realname}:{encrypted_password}\n')
#
#     print(f"User {username} created sucessfully.")


import codecs
import getpass
def add_user(data_file):
    with open(data_file, "rt") as data:
        existing_users = [line.split(":")[0] for line in data.readlines()]

    username = input("Enter your username: ")

    if username in existing_users:
        print("User already exists.")
        return

    realname = input("Enter your real name: ")
    print("Enter your password: ")
    password=getpass.getpass()

    encrypted_password = codecs.encode(password, "rot_13")

    with open(data_file, 'a') as file:
        file.writelines(f'{username}:{realname}:{encrypted_password}\n')

    print(f"User {username} created successfully.")

add_user("passwd.txt")