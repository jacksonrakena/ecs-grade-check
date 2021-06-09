LOG_FILE = "log.txt"


def log(string):
    f = open(LOG_FILE, "a")
    f.write(string)
    f.write("\n")
    f.close()


def print_log(string):
    print(string)
    log(string)


def clear():
    f = open(LOG_FILE, "w")
    f.close()
