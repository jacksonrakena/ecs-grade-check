from os.path import isfile

from cryptography.fernet import Fernet

SECRET_FILE = "userpass_secret.key"
USERNAME_FILE = "userpass_username.txt"
PASSWORD_FILE = "userpass_password.txt"


def generate_key():
    """
    Generates a key and saves it into a file
    """

    key = Fernet.generate_key()
    with open(SECRET_FILE, "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key named secret.key from the current directory
    :return: the key
    """
    if not isfile(SECRET_FILE):
        generate_key()

    return open(SECRET_FILE, "rb").read()


def save_data(file, data):
    """
    Save data to file, encrypting
    :param file: file to save to
    :param data: data to encrypt and save
    :return:
    """
    f = open(file, "wb")
    f.write(Fernet(load_key()).encrypt(data.encode()))
    f.close()


def get_data(file):
    """
    gets the data
    :param file: file to get from
    :return: the decrypted data
    """
    f = open(file, "rb")
    encrypted = f.read()
    return Fernet(load_key()).decrypt(encrypted).decode()


def save_password(password):
    save_data(PASSWORD_FILE, password)


def save_username(username):
    save_data(USERNAME_FILE, username)


def get_password() -> str:
    init()
    return get_data(PASSWORD_FILE)


def get_username() -> str:
    init()
    return get_data(USERNAME_FILE)


def init():
    if not isfile(SECRET_FILE):
        generate_key()

    if not isfile(USERNAME_FILE) or not isfile(PASSWORD_FILE):
        print("This is the first time running GetGrade. Please enter:")
        username = input("Username:")
        password = input("Password:")
        save_username(username)
        save_password(password)
