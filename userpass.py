from os.path import isfile
from cryptography.fernet import Fernet

SECRET_FILE = "userpass_secret.key"
EMAIL_FILE = "userpass_email_addr.txt"
USERNAME_FILE = "userpass_username.txt"
PASSWORD_FILE = "userpass_password.txt"


def _generate_key():
    """
    Generates a key and saves it into a file
    """

    key = Fernet.generate_key()
    with open(SECRET_FILE, "wb") as key_file:
        key_file.write(key)


def _load_key():
    """
    Loads the key named secret.key from the current directory
    :return: the key
    """
    if not isfile(SECRET_FILE):
        _generate_key()

    return open(SECRET_FILE, "rb").read()


def _save_data(file, data):
    """
    Save data to file, encrypting
    :param file: file to save to
    :param data: data to encrypt and save
    :return:
    """
    f = open(file, "wb")
    f.write(Fernet(_load_key()).encrypt(data.encode()))
    f.close()


def _get_data(file):
    """
    gets the data
    :param file: file to get from
    :return: the decrypted data
    """
    f = open(file, "rb")
    encrypted = f.read()
    return Fernet(_load_key()).decrypt(encrypted).decode()


def _save_password(password):
    _save_data(PASSWORD_FILE, password)


def _save_username(username):
    _save_data(USERNAME_FILE, username)


def _save_email_address(email_address):
    _save_data(EMAIL_FILE, email_address)


def get_password() -> str:
    """
    returns the users password, calling init() first
    :return: the password stored in the email file
    """
    _init()
    return _get_data(PASSWORD_FILE)


def get_username() -> str:
    """
    returns the users username, calling init() first
    :return: the username stored in the email file
    """
    _init()
    return _get_data(USERNAME_FILE)


def get_email_address() -> str:
    """
    returns the users email address, calling init() first
    :return: the email address stored in the email file
    """
    _init()
    return _get_data(EMAIL_FILE)


def _init():
    """
    Initialises the userpass. Queries the user if any of the files dont exist
    """
    if not isfile(SECRET_FILE):
        _generate_key()

    if not isfile(USERNAME_FILE) or not isfile(PASSWORD_FILE) or not isfile(EMAIL_FILE):
        print("This is the first time running GetGrade. Please enter:")
        email_addr = input("Email address to send to:")
        username = input("Username:")
        password = input("Password:")
        _save_email_address(email_addr)
        _save_username(username)
        _save_password(password)
