#
# import codecs
# import getpass
#
# def changepw(data_file):
#     info = []
#
#     with open(data_file, "r") as data:
#         for line in data:
#             info.append(line)
#
#     username = input("Enter your username:")
#     password = input("Enter your password:")
#     # password = getpass.getpass("Enter your password: ")
#     for i, user in enumerate(info):
#         existing_user = user.split(":")[0]
#         real_username = user.split(":")[1]
#         existing_password = user.split(":")[2]
#         encrypted_password = codecs.decode(existing_password.strip(), "rot_13")  # Ensure to strip whitespace
#
#         if username == existing_user:
#             if password == encrypted_password:
#                 new_password = input("Enter your new password:")
#                 encoded_new_pass = codecs.encode(new_password, "rot_13")
#                 info[i] = f"{username}:{real_username}:{encoded_new_pass}\n"
#                 with open(data_file, "w") as updated_file:
#                     updated_file.writelines(info)
#
#                 print("Password changed successfully.")
#                 return
#             else:
#                 print("Incorrect password.")
#                 return
#
#     print("Error: User not found or incorrect password.")

import codecs
import getpass

def change_password(data_file):
    with open(data_file, "r") as data:
        user_data = [line.strip().split(":") for line in data]

    username_to_change = input("Enter your username: ")
    print("Enter your current password: ")
    current_password=getpass.getpass()
    for user_info in user_data:
        existing_user, real_username, existing_password = user_info
        decrypted_password = codecs.decode(existing_password, "rot_13")

        if username_to_change == existing_user and current_password == decrypted_password:
            new_password = input("Enter your new password: ")
            encoded_new_password = codecs.encode(new_password, "rot_13")
            user_info[2] = encoded_new_password

            with open(data_file, "w") as updated_file:
                for user_info in user_data:
                    updated_file.write(f"{':'.join(user_info)}\n")

            print("Password changed successfully.")
            return

    print("Error: User not found or incorrect password.")
change_password("passwd.txt")


