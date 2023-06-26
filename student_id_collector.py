#!/usr/bin/env python

import csv 


def add_student():
    '''  Collect student's name, age, phone 
    and store the data into the csv file.. '''

    #open csv file in write mode 
    with open("data.csv", "a", newline='') as file:
        write = csv.writer(file)
        #get the number of student
        while True:
                try:
                    num_student = int(input("Number of student:  "))
                    break               
                except ValueError:
                    print("Error: Not a valid number")

        #collect the data    
        for i in range(num_student):
            print(f"----- student {i+1} -----")
            name = input(" Name: ")
            age = input(" Age: ")
            phone = input(" Phone: ")
            write.writerow([name,age,phone])  #write data row
                

    print("Data collection completed successfully. ")


def display_data():
    '''Display the data from the csv file'''

    with open("data.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader, 1):
            print(f"{i}. {' | '.join(row)}")


def remove_data():
    '''Remove a row from the CSV file'''
    rows = []
    with open("data.csv", "r", newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
    if not rows:
        print("No rows to remove")
        return
    #display data
    print("Current data:")
    display_data()
    #getting input from the user.
    try:
        row_number = int(input("Enter the row number to remove: "))

        if row_number == 0:
            print("Operation canceled.")
            return
        elif 1 <= row_number <= len(rows):  
            rows.pop(row_number - 1)

            with open("data.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Row removed successfully")
        else:
            print("Invalid row number")
    except ValueError:
        print("Invaild input. Enter a valid row number")



def main():

    while True:

        print("\nSelect the operation you want to perform:")
        print("(1) Add student info")
        print("(2) Display information")
        print("(3) remove student")
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
        else:
            print("Invalid operation")


if __name__ == "__main__":
    main()
