import random
import string
import sqlite3


def generate_password():
    """Generates a random password of specified length."""
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print("Generated Password is:", password)
    return password


def save_password(username, pagename, password):
    """Saves a username and password to the database."""
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS passwords (username text, pagename text, password text)")
    c.execute("INSERT INTO passwords VALUES (?, ?, ?)", (username, pagename, password))
    conn.commit()
    conn.close()


def get_password(username):
    """Retrieves the password for a given username from the database."""
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT username, pagename, password FROM passwords WHERE username=?", (username,))
    rows = c.fetchone()
    conn.close()

    if rows is not None:
        return rows[0], rows[1], rows[2]
    else:
        return None


def get_all_passwords():
    """Retrieves all passwords from the database."""
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT username, pagename, password FROM passwords")
    rows = c.fetchall()
    conn.close()
    if rows is not None:
        return rows
    else:
        return None


# Example usage: generate a 12-character password and save it to the database
def generate():
    user_name = input("Enter a User Name: ")
    page_name = input("Enter a User pagename: ")
    pass_word = generate_password()
    save_password(user_name, page_name, pass_word)

# Retrieve the password for the same user and print it
def retrive():
    a = input("\nEnter User_name to view Password: ")
    retrieved_password = get_password(a)
    print(retrieved_password)

'''
def view_all():
    # To print all passwords
    passwords = get_all_passwords()
    for row in passwords:
        print(row)
'''
