import getpass
from PyWagg import repl


def main():
    user = getpass.getuser()
    print("Hello %s! This is the Wagg programming language!" % user)
    print("Feel free to type in commands:")
    repl.start()


if __name__ == "__main__":
    main()
