#!/usr/bin/env python

import csv 


def add_student():
    '''  Collect student's name, age, phone 
    and store the data into the csv file.. '''

    #open csv file in write mode 
    with open("data.csv", "a", newline='') as file:
        write = csv.writer(file)
        write.writerow(["Name", "Age", "Phone"]) 
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
    '''removes data from the csv file '''
    with open("data.csv", "r", newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

        # display data
        print("Current Data: ")
        display_data()

        # getting the row number from user input
        while True:
            try:
                row_number = int(input("Enter the row number to remove ( 0 to cancel )"))
                if row_number == 0:
                    print("Operation Cancelled")
                    break
                elif 1 <= row_number <= len(data):
                    break
                else:
                    print("Invaild row number. Try again ")
            except ValueError:
                print("Invaild input. Please enter a vaild row number..")
        
        #remove the row
        removed_data = data.pop(row_number - 1)

        #modify the csv data 
        with open("data.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

        print(f"Row {row_number} removed successfully ")
        print(' | '.join(removed_data))




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
