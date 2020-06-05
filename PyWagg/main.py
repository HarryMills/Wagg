import getpass
from PyWagg import repl
from PyWagg import tokens


def main():
    user = getpass.getuser()
    print(tokens.keywords.get("floof"))
    print("Hello %s! This is the Wagg programming language!" % user)
    print("Feel free to type in commands:")
    repl.start()


if __name__ == "__main__":
    main()
