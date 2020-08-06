"""
Name: Alexander James Hing Chong Lynne
Date started: 08/06/2020
GitHub URL:

"""

MENU = ("Menu: \nL - List places \nA - Add new place \nQ - Quit")

def count_places(file):
    num_places = 0
    for row in file:
        num_places += 1
    return num_places



def main():
    print("Travel Tracker 1.0 - by Alexander Lynne")
    in_file = open("places.csv", "r")
    initial_num_places = count_places(in_file)
    print("{0} places loaded from places.csv".format(initial_num_places))

    print(MENU)

    menu_choice = input(">>> ").upper()
    while menu_choice not in ["L", "A", "Q"]:
        print("Invalid Menu Choice")
        menu_choice = input(">>> ").upper()


if __name__ == '__main__':
    main()
