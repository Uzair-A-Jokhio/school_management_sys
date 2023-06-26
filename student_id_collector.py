#!/usr/bin/env python
from improved_ui import clear_screen
from data_collector import display_data, modify_data, remove_data, add_student



def main():
    clear_screen()
    while True:

        print("\nSelect the operation you want to perform:\n")
        print("(1) Add student infotmation\n")
        print("(2) Display information\n")
        print("(3) Remove student data\n")
        print("(4) Modify student data\n")
        print("Enter 'q' to exit")

        print("---------------------------")
        x = input("Operation: ")
        print("---------------------------\n")

        if x == "q":
            break
        if x == "1":
            add_student()
        elif x == "2":
            display_data()
        elif x == "3":
            remove_data()
        elif x == "4":
            modify_data()
        else:
            print("Invalid operation")


if __name__ == "__main__":
    main()
