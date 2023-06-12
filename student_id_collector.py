#!/usr/bin/env python

student_data = {"name":[],
                "age":[],
                "phone":[],
                }

def student_id_collector(data):
    '''  Collect student's name, age, phone 
    and store the data '''

    x = 1 
    y = int(input("Total number of student: ")) # the total number of student 

    while x < y:
        print(f"=== Student NO {x} ===")
        # info details
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        phone = input("Enter phone number: ")
        # saving the data
        data["name"].append(name)
        data["age"].append(age)
        data["phone"].append(phone)
        
        x += 1
        
    
    return data 


