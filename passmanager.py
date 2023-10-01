import random
import string
import sqlite3

# funzione per generare la password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# funzione per generare la tabella
def create_passwords_table():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

# funzione per inserire una password nel database 
def insert_password(password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (password) VALUES (?)", (password,))
    conn.commit()
    conn.close()

# funzione per vedere le password gia' salvate
def get_passwords():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords")
    passwords = cursor.fetchall()
    conn.close()
    return passwords

# Int Main
if __name__ == "__main__":
    create_passwords_table()

    while True:
        print("Options:")
        print("1. Generate Password")
        print("2. View Stored Passwords")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            length = int(input("Enter the length of the password: "))
            password = generate_password(length)
            insert_password(password)
            print(f"Generated Password: {password}")
        elif choice == "2":
            passwords = get_passwords()
            if passwords:
                print("Stored Passwords:")
                for row in passwords:
                    print(row[1])
            else:
                print("No passwords stored yet.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose a valid option.")
