from pathlib import Path
import json 
contact_info = {}
class ContactBook:
    '''setting the default attributes for the class'''
    def __init__(self,name,number,email,dob):
        self.name = name 
        self.number = number 
        self.email = email 
        self.dob = dob
    #create the create contact 
    def create_contact(self):
        contact_info[self.name] = {}
        contact_info[self.name]['number'] = self.number 
        contact_info[self.email]['email'] = self.email 
        contact_info[self.dob]['dob'] - self.dob 
        print("created the contact")
    #method to view contact 
    def view_contact(self): 
        print("\n--LIST OF YOUR CONTACT-----\n")
        for contact in contact_info:
            print(f"Contact details of {contact}")
            for key,value in contact_info[self.name].items():
                print(f"\n{key} -> {value}")
    #method to search contact
    def search_contact(self):
        print("--------SEARCH---------- ")
        contact_name = input("please enter the name you want to search: ")
        for contact in contact_info:
            if contact == contact_name:
                for key,value in contact_info[self.name].items():
                    print(f"\n{key} -> {value}")
            else:
                print("searching...")
    #method to update contact
    def update_contact(self):
        print("-----UPDATE CONTACT---------")
        contact_name = input("please enter the name you want to edit: ")
        for contact in contact_info:
            if contact == contact_name:
                for key,value in contact_info[self.name].items():
                    print(f"\n{key} -> {value}")
                    print(f"these are the current infomation about {contact_name}")
                    print("1>name\n2>number\n3email\n4>dob")
                    choice = input("enter the details you want to edit: ")
                    match choice:
                        case '1':
                            updated_name = input("please enter the updated name: ")
                            contact_info[self.name] = updated_email
                        case '2':
                            updated_number = input("please enter the updated number: ")
                            contact_info[self.name]['number'] = updated_number
                        case '3':
                            updated_email = input("please enter the updated email: ")
                            contact_info[self.name]['email'] = updated_email
                        case '4':
                            updated_dob = input("please enter the updated dob 'd-m-y' format: ")
                            contact_info[self.dob] = updated_dob
                        case '':
                            print("please select the correct option")
            else:
                print("searching...")
    #method to delete the contact 
    def delete_contact(self):
        

                