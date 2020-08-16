"""

Name: Alexander James Hing Chong Lynne
Date started: 08/06/2020
GitHub URL: https://github.com/tilsies/assignment-1-travel-tracker-tilsies

"""
from operator import itemgetter

MENU = ("Menu: \nL - List places \nA - Add new place \nM - Mark a place as visited \nQ - Quit")
FILENAME = "places.csv"


def get_data(input_file):
    """
    Creates initial list of list
    Strips lines into seperate list
    Splits elements by "," in csv
    Appends a 5th element of "*" or " " based on 4th element of list.
    """

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
    """
    Prints data in readable format
    """

    index = 0
    for details in data:
        index += 1
        print("{5:1}{0}. {1:10} in {2:15} priority {3:>3}".format(index, *details))


def count_unvisited(data):
    """
    Takes input parameter (data) and returns number of unvisited places
    """
    count = sum(n.count("n") for n in data)
    return count

def sort_data(data):
    """
    Takes input parameter (data) and returns data sorted Unvisited/Visited followed by Priority
    """
    data.sort(key=itemgetter(3,2))
    return data

def add_entry():
    """
    Takes inputs for adding new entry and returns list.
    """
    new_location = []

    city_name = input("City name: ").capitalize()
    while len(city_name) <= 0:
        print("Input can not be blank")
        city_name = input("City name: ").capitalize()
    new_location.append(city_name)

    country_name = input("Country: ").capitalize()
    while len(country_name) <= 0:
        print("Input can not be blank")
        country_name = input("Country: ").capitalize()
    new_location.append(country_name)

    priority = input("Priority: ")
    while not priority.isnumeric() or priority <= "0":
        print("Invalid input; enter a valid number")
        priority = input("Priority: ")
    new_location.append(priority)

    visited = input("Have you visited this country? (v/n): ".lower())
    while visited not in ["v", "n"]:
        print("Inavlid input; enter a valid option")
        visited = input("Have you visited this country? (v/n): ".lower())
    new_location.append(visited)

    if new_location[3] == "n":
        new_location.append("*")
    else:
        new_location.append("")

    return new_location


def mark_visited(data):
    """
    Takes input parameter (data)
    Takes user input to select sublist in data
    Updates entry to visited if country selected is currently unvisited
    """
    while True:
        try:
            mark_visited = int(input("Enter the number of a place to mark as visited \n>>> ")) - 1
            break
        except ValueError:
            print("Invalid input, enter a valid number")

    while mark_visited > len(data) - 1:
        print("Invalid place number")
        mark_visited = int(input("Enter the number of a place to mark as visited \n>>> ")) - 1

    if data[mark_visited][3] == "v":
        print("That place is already visited \n")

    else:
        data[mark_visited][3] = "v"
        data[mark_visited][4] = ""
        print("{0} in {1} visited! \n".format(data[mark_visited][0], data[mark_visited][1]))

    return data


def remove_last(data):
    """
    Removes 5th element of "*" / " " from sublist in data
    """
    for sublist in data:
        del sublist[-1]

    return data


def main():
    print("Travel Tracker 1.0 - by Alexander Lynne")
    input_file = open(FILENAME)
    data = get_data(input_file)
    print("{0} places loaded from {1}".format(len(data), FILENAME))

    print(MENU)

    menu_choice = input(">>> ").upper()
    while menu_choice not in ["L", "A", "M", "Q"]:
        # Error checking for inputs
        print("Invalid Menu Choice")
        menu_choice = input(">>> ").upper()

    while menu_choice in ["L", "A", "M"]:
        if menu_choice == "L":
            # Sorts data and prints in readable format. Also prints count of unvisited locations
            sort_data(data)
            display_data(data)
            num_unvisited = count_unvisited(data)
            print("{0} places. You still want to visit {1} places.".format(len(data), num_unvisited))

        elif menu_choice == "A":
            # Creates new list using add_entry() and appends list to data. Sorts appended list and prints in format
            new_entry = add_entry()
            data.append(new_entry)
            sort_data(data)
            print("{0} in {1} (priority {2}) added to Travel Tracker".format(*new_entry))


        else:
            # Checks if all places are visited. If true prints all places are visited, if false allows user to mark place as visited
            elem_to_find = "*"
            all_visited = any(elem_to_find in sublist for sublist in data)

            if all_visited == False:
                print("\nNo unvisited places \n")

            else:
                display_data(data)
                num_unvisited = count_unvisited(data)
                print("{0} places. You still want to visit {1} places.".format(len(data), num_unvisited))
                mark_visited(data)
                sort_data(data)

        print(MENU)
        menu_choice = input(">>> ").upper()
        while menu_choice not in ["L", "A", "M", "Q"]:
            print("Invalid Menu Choice")
            menu_choice = input(">>> ").upper()

    if menu_choice == "Q":
        # Removes added element of "*"/" " from sublist and saves files in appropriate format
        remove_last(data)
        output_file = open(FILENAME, "w")

        save_index = 0
        for sublist in data:
            save_index = 0
            for element in sublist:
                save_index += 1

                if save_index < len(sublist):
                    output_file.write(element)
                    output_file.write(",")
                else:
                    output_file.write(element)
            output_file.write("\n")


        print("{0} places saved to places.csv \nHave a nice day :D".format(len(data)))


if __name__ == '__main__':
    main()
