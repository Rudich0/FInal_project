#

# def login(data_file):
#     info = []
#
#     with open(data_file, "r") as data:
#         for line in data:
#             info.append(line.strip())
#
#     username = input("Enter your username: ")
#
#     for user in info:
#         existing_username, real_username, existing_password= user.split(":")
#         encrypted_password = codecs.decode(existing_password, "rot_13")
#         if username == existing_username:
#             count = 0
#             while count < 3:
#                 password = input("Enter your password: ")
#                 #password = getpass.getpass("Enter your password: ")
#                 if password == encrypted_password:
#                     print(f"Login successful for user {username}")
#                     print(f"Welcome {real_username}")
#                     return
#                 else:
#                     print("Incorrect Password. Try again.")
#                     count += 1
#                     print(f"{3 - count} attempts left.")
#
#             print("0 attempts left. Redirecting to the Main menu.")
#             return
#
#     print("Login failed: User not found.")


import codecs
import getpass

def get_user_info(user_data, username):
    for user_info in user_data:
        existing_username, real_username, existing_password = user_info.split(":")
        decrypted_password = codecs.decode(existing_password, "rot_13")

        if username == existing_username:
            return real_username, decrypted_password

    return None, None

def login_user(data_file):
    user_data = []

    with open(data_file, "r") as data:
        for line in data:
            user_data.append(line.strip())

    username_to_login = input("Enter your username: ")
    real_username, decrypted_password = get_user_info(user_data, username_to_login)

    if real_username is not None:
        login_attempts = 3
        while login_attempts > 0:
            print("Enter your password: ")
            entered_password = getpass.getpass()
            if entered_password == decrypted_password:
                print(f"Login successful for user {username_to_login}")
                print(f"Welcome {real_username}")
                return
            else:
                print("Incorrect Password. Try again.")
                login_attempts -= 1
                print(f"{login_attempts} attempts left.")

        print("Incorrect Passwords Entered. Try again Later")
    else:
        print("Login failed: User not found.")

login_user("passwd.txt")