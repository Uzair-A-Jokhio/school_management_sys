#!/usr/bin/env python

student_data = {"name":[],
                "age":[],
                "phone":[],
                }

def add_student(data):
    '''  Collect student's name, age, phone 
    and store the data '''

    x = 0 
    y = int(input("Total number of student: ")) # the total number of student 

    while x < y:
        print(f"====== Student NO {x+1} ======")
        # info details
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        phone = input("Enter phone number: ")
        # saving the data
        data["name"].append(name)
        data["age"].append(age)
        data["phone"].append(phone)
        
        x += 1
        
    print("----------------------------------------")
    return data 


def display_student(data):
    if data:
        print("list of students: ")
        for i, student in enumerate(data["name"]):
            print(f"S.No: {i + 1} ")
            print(f"Name: {student}")
            print(f"Age: {data['age'][i]}")
            print(f"Phone: {data['phone'][i]}")
            print("----------------------------------------")
    else:
        print("No data in the system...")



def main():

    while True:
        print("\n Select the correct Operation you want to perform (1, 2, etc..) to exit q\n")
        print(" (1) Adding student info.. ")
        print(" (2) Display information..  \n")
        
        print("===========================")
        x = input("Operation: ")
        print("===========================")

        info = student_data

        if x == "q":
            break

        if x == "1":
            info = add_student(info)
        elif x == "2":
            display_student(info)
        else:
            print("Invalid Operation")
        




if __name__ == "__main__":
    main()
