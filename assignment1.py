"""
Name: Alexander James Hing Chong Lynne
Date started: 08/06/2020
GitHub URL:

"""

MENU = ("Menu: \nL - List places \nA - Add new place \nQ - Quit")
FILENAME = "places.csv"

def get_data():
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(",")
        if parts[3] == "n":
            parts.append("*")
        else:
            parts.append("")
        data.append(parts)
    input_file.close()
    return data

def display_data(data):
    index = 0
    for details in data:
        index += 1
        print("{5:1}{0}. {1:10} in {2:15} priority {3:>3}".format(index, *details))

def count_unvisited(data):
    count = sum(n.count("n") for n in data)
    return count


def main():
    print("Travel Tracker 1.0 - by Alexander Lynne")
    data = get_data()
    print("{0} places loaded from {1}".format(len(data), FILENAME))

    print(MENU)

    menu_choice = input(">>> ").upper()
    while menu_choice not in ["L", "A", "Q"]:
        print("Invalid Menu Choice")
        menu_choice = input(">>> ").upper()

    while menu_choice in ["L", "A", "Q"]:
        if menu_choice == "L":
            display_data(data)
            num_unvisited = count_unvisited(data)
            print("{0} places. You still want to visit {1} places.".format(len(data), num_unvisited))

        else:
            continue

        menu_choice = input(">>> ").upper()

            




if __name__ == '__main__':
    main()
