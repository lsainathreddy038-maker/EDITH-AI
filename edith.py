"""
EDITH AI
Main Entry Point
Version: 7.0
Author: Sai Nath Reddy
"""

from datetime import datetime

VERSION = "7.0"

class Edith:

    def __init__(self, user):
        self.user = user

    def hello(self):
        print(f"EDITH: Hello {self.user}!")

    def time(self):
        print("EDITH:", datetime.now().strftime("%I:%M:%S %p"))

    def date(self):
        print("EDITH:", datetime.now().strftime("%d %B %Y"))

    def help(self):
        print("""
Commands
--------
hello
time
date
help
exit
""")

def main():

    print("=" * 50)
    print("      EDITH AI Version", VERSION)
    print("=" * 50)

    user = input("Enter your name: ")

    edith = Edith(user)

    while True:

        cmd = input("\nYou: ").lower().strip()

        if cmd == "hello":
            edith.hello()

        elif cmd == "time":
            edith.time()

        elif cmd == "date":
            edith.date()

        elif cmd == "help":
            edith.help()

        elif cmd == "exit":
            print("EDITH: Goodbye!")
            break

        else:
            print("EDITH: Unknown command.")

if __name__ == "__main__":
    main()