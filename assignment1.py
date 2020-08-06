"""
Name: Alexander James Hing Chong Lynne
Date started: 08/06/2020
GitHub URL:

"""

MENU = print("Menu: \nL - List places \nA - Add new place \nQ - Quit")

def main():
    print("Travel Tracker 1.0 - by <Your Name>")

    MENU

    menu_choice = input(">>> ").upper()
    while menu_choice not in ["L", "A", "Q"]:
        print("Invalid Menu Choice")
        menu_choice = input(">>> ").upper()


if __name__ == '__main__':
    main()
