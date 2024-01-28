#
# import codecs
# import getpass
# def delusr(data_file):
#     info = []
#
#     with open(data_file, "r") as data:
#         for line in data:
#             info.append(line.strip())
#
#     username = input("Enter your username: ")
#     # password = getpass.getpass("Enter your password: ")
#     password = input("Enter your password: ")
#
#     for i, line in enumerate(info):
#         existing_user = line.split(":")[0]
#         existing_password = line.split(":")[2]
#         encrypted_password = codecs.decode(existing_password, "rot_13")
#
#         if username == existing_user:
#             if password == encrypted_password:
#                 info.pop(i)
#                 print(f"User '{username}' deleted successfully.\n")
#                 with open(data_file, "w") as data:
#                     for item in info:
#                         data.write(f"{item}\n")
#                 return
#             else:
#                 print("Incorrect password.")
#                 return
#
#     print("User not found.")



import codecs
import getpass

def delete_user(data_file):
    username = input("Enter your username: ")
    print("Enter your password: ")
    password=getpass.getpass()

    with open(data_file, "r") as data:
        user_data = [line.strip() for line in data]

    for i, user_info in enumerate(user_data):
        existing_user, _, existing_password = user_info.split(":")
        decrypted_password = codecs.decode(existing_password, "rot_13")

        if username == existing_user and password == decrypted_password:
            del user_data[i]
            with open(data_file, "w") as updated_data:
                updated_data.write("\n".join(user_data))
            print(f"User '{username}' deleted successfully.\n")
            return
    print("User not found or incorrect password.")

delete_user("passwd.txt")
