from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
''' 

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)   

def view():
    try:
        with open("passwords.txt", "r") as f:  # Changed from 'a' to 'r'
            for line in f.readlines():
                data = line.rstrip()
                if "|" in data:
                    user, pwd = data.split("|")
                    print(f"Account: {user}, Password: {fer.decrypt(pwd.encode()).decode()}")
                else:
                    print("Malformed line:", data)
    except FileNotFoundError:
        print("No passwords found. Add some first.")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view), or 'q' to quit: ").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please choose 'add' or 'view'.")
