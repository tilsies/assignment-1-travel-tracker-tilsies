"""
Name: Alexander James Hing Chong Lynne
Date started: 08/06/2020
GitHub URL:

"""

MENU = ("Menu: \nL - List places \nA - Add new place \nM - Mark a place as visited \nQ - Quit")
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

def add_entry():
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

    visited = input("Have you visited this country? (v/n)".lower())
    while visited not in ["v", "n"]:
        print("Inavlid input; enter a valid option")
        visited = input("Have you visited this country? (v/n)".lower())
    new_location.append(visited)

    if new_location[3] == "n":
        new_location.append("*")
    else:
        new_location.append("")

    return new_location



def main():
    print("Travel Tracker 1.0 - by Alexander Lynne")
    data = get_data()
    print("{0} places loaded from {1}".format(len(data), FILENAME))

    print(MENU)

    menu_choice = input(">>> ").upper()
    while menu_choice not in ["L", "A", "M", "Q"]:
        print("Invalid Menu Choice")
        menu_choice = input(">>> ").upper()

    while menu_choice in ["L", "A", "M"]:
        if menu_choice == "L":
            display_data(data)
            num_unvisited = count_unvisited(data)
            print("{0} places. You still want to visit {1} places.".format(len(data), num_unvisited))

        elif menu_choice =="A":
            new_entry = add_entry()
            data.append(new_entry)
            print("{0} in {1} (priority {2}) added to Travel Tracker".format(*new_entry))


        else:
            continue

        print(MENU)
        menu_choice = input(">>> ").upper()

    if menu_choice == "Q":
        print("placeholder") #TODO complete

            




if __name__ == '__main__':
    main()
