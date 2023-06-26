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
    '''displays the data from the csv file'''

    with open("data.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)




def main():

    while True:

        print("\nSelect the operation you want to perform:")
        print("(1) Add student info")
        print("(2) Display information")
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
        else:
            print("Invalid operation")


if __name__ == "__main__":
    main()
