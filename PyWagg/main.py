import getpass
from PyWagg import repl
from PyWagg import tokens


def main():
    user = getpass.getuser()
    print(tokens.keywords.get("floof"))
    print("Hello %s! This is the Wagg programming language!\n" % user)
    print("Feel free to type in commands\n")
    repl.start()


if __name__ == "__main__":
    main()
