import csv 
from tabulate import tabulate
import shutil
from improved_ui import clear_screen



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
    print("Displaying Data:\n")

    with open("data.csv", "r", newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        
        # Generate a numbered list of rows
        numbered_data = [[str(i)] + row for i, row in enumerate(data, 1)]

        # Display the data using tabulate
        print(tabulate(numbered_data, headers=["#", "Name", "Age", "Phone"], tablefmt="fancy_grid"))


def remove_data():
    '''Remove a row from the CSV file'''
    clear_screen()
    print("Removing Student Data:\n")

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
        row_number = int(input("Enter the row number to remove(0 to cancel): "))
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


def modify_data():
    ''' modify a row in a csv file '''
    clear_screen()
    print("Modifying Student Data:\n")

    rows = []
    with open("data.csv", 'r',newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        print("no row to modify")
        return
    
    print("Current Data")
    display_data()

    try:
        row_number = int(input("Enter the Row number (0 to cancel): "))

        if 1 <= row_number <= len(rows):
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            phone = input("Enter New Phone: ")
            rows[row_number -1] =[name,age,phone]

            with open("data.csv","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("\nRow modified successfully")

        elif row_number == 0:
            print("Operation cancelled. ")

        else:
            print("Invalid row number. ")

    except ValueError:
        print("Invalid row number Please try again ")
