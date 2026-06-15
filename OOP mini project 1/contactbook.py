from pathlib import Path
import json 
contact_info = {}

path = Path(r'C:\Users\Envay\Desktop\python\OOP mini project 1\contact.json')
class ContactBook:
    '''setting the default attributes for the class'''
    def __init__(self,name='',number='',email='',dob=''):
            self.name = name 
            self.number = number 
            self.email = email 
            self.dob = dob
    #create the create contact 
    def create_contact(self):
        self.read_file()
        contact_info[self.name] = {}
        contact_info[self.name]['number'] = self.number 
        contact_info[self.name]['email'] = self.email 
        contact_info[self.name]['dob'] = self.dob 
        self.save_mod()
        print("created the contact")
    #method to view contact 
    def view_contact(self): 
        print("\n--LIST OF YOUR CONTACT-----\n")
        self.read_file()
        for contact in contact_info:
            print(f"Contact details of {contact}")
            for key,value in contact_info[contact].items():
                print(f"\n{key} -> {value}")
    #method to search contact
    def search_contact(self):
        print("--------SEARCH---------- ")
        self.read_file()
        contact_name = input("please enter the name you want to search: ")
        if contact_name in contact_info:
            for key,value in contact_info[contact_name].items():
                    print(f"\n{key} -> {value}")
        else:
            print("searching...")
    #method to update contact
    def update_contact(self):
        print("-----UPDATE CONTACT---------")
        self.read_file()
        contact_name = input("please enter the name you want to edit: ")
        if contact_name in contact_info:
            for key,value in contact_info[contact_name].items():
                print(f"\n{key} -> {value}")
                print(f"these are the current infomation about {contact_name}")
                print("1>name\n2>number\n3email\n4>dob")
                choice = input("enter the details you want to edit: ")
                match choice:
                    case '1':
                        updated_name = input("please enter the updated name: ")
                        contact_info[contact_name] = updated_name
                        self.save_mod()
                            
                    case '2':
                        updated_number = input("please enter the updated number: ")
                        contact_info[contact_name]['number'] = updated_number
                        self.save_mod()
                    case '3':
                        updated_email = input("please enter the updated email: ")
                        contact_info[contact_name]['email'] = updated_email
                        self.save_mod()
                    case '4':
                        updated_dob = input("please enter the updated dob 'd-m-y' format: ")
                        contact_info[contact_info] = updated_dob
                        self.save_mod()
                    case '':
                        print("please select the correct option")
        else:
            print("Not found")
    #method to delete the contact 
    def delete_contact(self):
        select_contact = input("select the contact you want to delete: ")
        if select_contact in contact_info:
            del contact_info[select_contact]
        else: 
            print('no contact found')
    ##save new modification in the contact app 
    def save_mod(self):
        content = json.dumps(contact_info)
        path.write_text(content)
    def read_file(self):
        global contact_info
        try:
            contact_info = json.loads(path.read_text())
        except:
            contact_info = {}
        
def main():
    print("\n------WELCOME TO THE CONTACT BOOK----------\n")
    cont1 = ContactBook()
    while True:
        print("1>Add Contact\n2.View all contact\n3>Search Contact\n4>Update Contact\n5>Delete Contact\n>5.Exit")
        choice = input("select the option from above: ")
        match choice: 
            case '1':
                name = input("please enter the name of the contact: ")
                try:
                    number_enter = int(input("enter the number"))
                except ValueError:
                    print("please enter the number: ")
                else: 
                    number = number_enter
                email= input("please enter the email: ")
                dob_set = input("please enter the dob in 'd-m-y' format: ")
                # dob_list = int(dob_set.split('-'))
                # if dob_list[0] > 32 or dob_list[0] <1:
                #     print("please select the correct day")
                # if dob_list[1]>12 or  dob_list[1]<1:
                #     print ("please select the correct month")
                # if dob_list[2] > 2026:
                #     print("please select the correct year")
                # else: 
                dob = dob_set 
                contact1 = ContactBook(name,number,email,dob)
                contact1.create_contact()

            case '2':
                cont1.view_contact()
            case '3':
                cont1.search_contact()
            case '4':
                cont1.update_contact()
            case '5':
                cont1.delete_contact()
            case '6':
                print("logging out..")
                break
main()