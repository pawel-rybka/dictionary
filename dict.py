import re
import os.path

MENU = """
Dictionary for a little programmer:
1) search explanation by appellation
2) add new definition
3) show all appellations alphabetically
4) show available definitions by first letter of appellation
0) exit
"""
FILE_NAME = "dict"
SEARCH = "1"
ADD = "2"
SHOW = "3"
SHOW_FIRST_LETTER = "4"
EXIT = "0"


def main():

    file_open = False
    if not os.path.isfile(FILE_NAME):
        print("Where is '{}' file?".format(FILE_NAME))
        exit()

    while True:
        print(MENU)
        while True:
            option = input()
            if re.match("[0-4]$", option):
                break
            print("Enter a valid number!")
        print("")

        if option == EXIT:
            exit()

        if not file_open:
            dict_file = open(FILE_NAME, "r")
            dictionary = {}
            for line in dict_file.readlines()[1:]:
                line = line[:-1]
                line = line.split(",\"")
                dictionary[line[0].lower()] = line[1][:-1], line[2][:-1]
                # dictionary[line[0]] = line[1][:-1], line[2][:-1]
            dict_file.close()
            file_open = True

        if option == SEARCH:
            search_key = input("Enter appellation: ").lower()
            if search_key in dictionary:
                print("\n{0} - {1}\n{2}".format(search_key,
                                                dictionary[search_key][0],
                                                dictionary[search_key][1]))
            else:
                print("\nNo such appellation found.")

        elif option == ADD:
            while True:
                add_key = input("Enter appellation: ").lower()
                if add_key == "":
                    print("Accept only non empty appellation.\n")
                elif add_key in dictionary:
                    print("Appellation already exists.\n")
                else:
                    break

            add_explanation = input("Enter explanation: ")
            add_source = input("Enter source: ")
            dictionary[add_key] = add_explanation, add_source
            dict_file = open(FILE_NAME, "a")
            dict_file.write("{0},\"{1}\",\"{2}\"\n".format(add_key,
                                                           add_explanation,
                                                           add_source))
            dict_file.close()

        elif option == SHOW:
            # sorted_list = sorted(dictionary)
            # sorted_list = sort_bubble_dict(dictionary)
            sorted_list = sort_dict(dictionary)
            for word in sorted_list:
                print(word)

        elif option == SHOW_FIRST_LETTER:
            first_letter = input("Enter first letter of appellation: ").lower()
            first_letter_found = False
            print("")
            for word in dictionary:
                if word[0] == first_letter:
                    print(word)
                    first_letter_found = True
            if not first_letter_found:
                print("No appellation found.")

        input("\nPress return to enter menu.")


def sort_bubble_dict(dictionary):
    """Sort dictionary in bubble way."""
    sort = False
    sort_list = []

    for word in dictionary:
        sort_list.append(word)

    while not sort:
        sort = True
        index = 0
        while index < len(sort_list) - 1:
            if sort_list[index] > sort_list[index+1]:
                item = sort_list[index]
                sort_list[index] = sort_list[index+1]
                sort_list[index+1] = item
                sort = False
            index += 1

    return sort_list


def sort_dict(dictionary):
    """Sort dictionary"""
    sort_list = []

    for word in dictionary:
        sort_list.append(word)
        index = len(sort_list) - 1

        while index > 0 and sort_list[index] < sort_list[index-1]:
            item = sort_list[index]
            sort_list[index] = sort_list[index-1]
            sort_list[index-1] = item
            index -= 1

    return sort_list

main()
