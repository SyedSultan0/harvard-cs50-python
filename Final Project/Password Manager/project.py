from cryptography.fernet import Fernet
import json
import hashlib
import sys
import requests

from colorama import Fore, Style, init
from email_validator import validate_email, EmailNotValidError
from zxcvbn import zxcvbn



# LOAD DATA


def load_data():
    try:
        with open("restricted.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# HASHING


def hashing(a):
    n = a.encode()
    m = hashlib.sha256()
    m.update(n)
    m.digest()
    return m.hexdigest()



# PASSWORD SETUP


def password():
    a = input("Enter password: ")
    h = hashing(a)

    key = Fernet.generate_key()

    FILE = "restricted.json"

    try:
        with open(FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data["Hashed_Master_Password"] = h
    data["Key"] = key.decode()

    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)



# CHECK LOGIN


def checking(a):
    user_hash = hashing(a)
    data = load_data()

    return user_hash == data.get("Hashed_Master_Password")



# ADD ACCOUNT


def add_account():
    try:
        with open("accounts.json", "r") as file:
            accounts_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        accounts_data = {}

    with open("restricted.json", "r") as file:
        restricted_data = json.load(file)

    more = True

    while more:
        account = input("Enter account name (google/apple/etc): ")

        try:
            mail = input("Enter email: ")
            validate_email(mail)
        except EmailNotValidError:
            print(Fore.RED + f"❌ INVALID EMAIL!")
            return

        pwd = input("Enter password: ")

        if not pwd:
            print(Fore.RED + f"❌ INVALID ENTRY!")
            return

        key = restricted_data["Key"].encode()
        f = Fernet(key)
        encrypted = f.encrypt(pwd.encode()).decode()

        accounts_data[account] = {
            "gmail": mail,
            "password": encrypted
        }

        with open("accounts.json", "w") as file:
            json.dump(accounts_data, file, indent=4)

        print("Account saved successfully!")

        a = input("Wanna add more Acounts?yes or no?: ")
        if a == "no":
            print("THANK U!")
            more = False



# SEARCH ACCOUNT

def search_account():
    a = input("Account?: ")

    try:
        with open("accounts.json", "r") as file:
            accounts_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No accounts found!")
        return

    try:
        with open("restricted.json", "r") as file:
            restricted_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("System error: missing encryption key!")
        return

    try:
        password = accounts_data[a]["password"]
        mail = accounts_data[a]["gmail"]
    except KeyError:
        print("Account not found!")
        return

    key = restricted_data["Key"].encode()
    f = Fernet(key)
    decrypted = f.decrypt(password.encode()).decode()

    print(f"📧 Email: {mail}")
    print(f"🔑 Password: {decrypted}")
    print("-" * 40)


# DELETE ACCOUNT


def delete_account():
    account_to_delete = input("Enter account name to delete: ")

    with open("accounts.json", "r") as file:
        data = json.load(file)

    if account_to_delete in data:
        del data[account_to_delete]
        print("Deleted successfully!")
    else:
        print("Account not found!")

    with open("accounts.json", "w") as file:
        json.dump(data, file, indent=4)



# PASSWORD STRENGTH


def check_password_strength():
    password = input("Enter Your Password: ")
    result = zxcvbn(password)

    print("\n🔐 PASSWORD ANALYSIS REPORT")
    print("=" * 40)

    score = result["score"]
    levels = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"]

    print(f"📊 Strength Score: {score}/4 ({levels[score]})")
    print(f"⏱️ Estimated Crack Time: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")

    feedback = result["feedback"]

    if feedback["warning"]:
        print(f"\n⚠️ Warning: {feedback['warning']}")

    if feedback["suggestions"]:
        print("\n💡 Suggestions:")
        for tip in feedback["suggestions"]:
            print(f"   • {tip}")

    print("=" * 40)

    return score



# BREACH CHECK


def breach():
    init()
    password = input("Enter password: ")

    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    hashes = response.text.splitlines()

    for line in hashes:
        h, count = line.split(":")

        if h == suffix:
            print(Fore.RED + f"❌ Password found in leaks {count} times!")
            return True

    print(Fore.GREEN + "✅ Password not found in leaks")
    return False



# MAIN


def main():
    new = input("SIGNIN(s) OR LOGIN(l):l or s: ").strip().lower()

    if new == "s":
        password()

    elif new == "l":
        login = input("ENTER MASTER PASSWORD: ")

        if checking(login):

            print("\n" + "=" * 45)
            print("🔐        PASSWORD MANAGER        🔐")
            print("=" * 45)

            print("1️⃣  ➕  Add Account")
            print("2️⃣  🔍  Search Account")
            print("3️⃣  ❌  Delete Account")
            print("4️⃣  🛡️  Check Password Strength")
            print("5️⃣  🕵️  Have I Been Pwned?HIBW")
            print("6️⃣  🚪  Exit")

            print("\n" + "=" * 45)

            option = input("📌 Please choose an option:\n").strip().lower()

            if option == "1":
                add_account()

            elif option == "2":
                search_account()

            elif option == "3":
                delete_account()

            elif option == "4":
                check_password_strength()

            elif option == "5":
                breach()

            elif option == "6":
                sys.exit("")

            else:
                print(Fore.RED + f"❌ INVALID OPTION!")


if __name__ == "__main__":
    main()
