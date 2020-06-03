import getpass
from PyWagg import token


def main():
    user = getpass.getuser()
    print(token.keywords.get("floof"))
    print("Hello %s! This is the Wagg programming language!\n" % user)
    print("Feel free to type in commands\n")
    # repl.start(interpreter)


if __name__ == "__main__":
    main()
