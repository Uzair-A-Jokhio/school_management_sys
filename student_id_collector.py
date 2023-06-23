#!/usr/bin/env python

import csv 


def add_student():
    '''  Collect student's name, age, phone 
    and store the data into the csv file.. '''

    #open csv file in write mode 
    with open("data.csv", "w", newline='') as file:

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
            write.writerow([name,age])  #write data row
                

    print("Data collection completed successfully. ")

def display_data():
    '''display'''

 





def main():

    while True:
        print("\n Select the correct Operation you want to perform (1, 2, etc..) to exit q\n")
        print(" (1) Adding student info.. ")
        print(" (2) Display information.. ")
        print(" (3) Remove student..  ")
        
        print("\n---------------------------")
        x = input("Operation: ")
        print("---------------------------\n")

        if x == "q":
            break

        if x == "1":
            info = add_student()
        else:
            print("Invalid Operation")
        

if __name__ == "__main__":
    main()
