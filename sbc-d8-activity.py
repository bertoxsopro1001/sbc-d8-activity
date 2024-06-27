def create_user():
    user = input("Enter Username: ")
    password = input("Enter Password: ")

    with open("accounts.txt", "a") as cf:
        cf.write(f"{user},{password}\n")

def login_user():
    user_login = input("Enter Username: ")
    user_pass = input("Enter Password: ")
    with open("accounts.txt", "r") as n_file:
        for line in n_file:
            stored_user, stored_pass = line.strip().split(',')
            if stored_user == user_login and stored_pass == user_pass:
                print("Login successful!")
                return
        print("Invalid username or password.")

def change_password():
    user_login = input("Enter Username: ")
    old_pass = input("Enter Current Password: ")
    new_pass = input("Enter New Password: ")
    with open("accounts.txt", "r") as n_file:
        lines = n_file.readlines()
    found = False
    with open("accounts.txt", "w") as cf:
        for line in lines:
            stored_user, stored_pass = line.strip().split(',')
            if stored_user == user_login and stored_pass == old_pass:
                cf.write(f"{user_login},{new_pass}\n")
                print("Password changed successfully!")
                found = True
            else:
                cf.write(f"{stored_user},{stored_pass}\n")
    
    if not found:
        print("Invalid username or password.")

def main():
    while True:
        print("\n1. Create User\n2. Login\n3. Change Password\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_user()
        elif choice == 2:
            login_user()
        elif choice == 3:
            change_password()
        elif choice == 4:
            break
        else:
            print("invalid choice")


main()
