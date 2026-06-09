user_info={}
user_list=[]

class Todo: 
    def __init__(self,user_name,password):
        self.user_name = user_name 
        self.password = password 
    def create_account(self):
        user_info['user_name'] = self.user_name 
        user_info['password'] = self.password
        user_info['tasks'] = []
        print(f"Welcome {self.user_name} your account has been created successfully")
    def create_task(self):
        while True: 
            task = input("please enter the task you want top save: ")
            if task == 'q':
                print("thanks!!! stay productive")
                break 
            else: 
                user_info['tasks'].append(task)
                print("task has been added")
    def see_task(self):
        i = 1
        for task in user_info['tasks']:
            print(f"{i}-> {task}")
            i += 1
    def delete_task(self):
        print("select the task you want to delete")
        select_task = input("please select the task you want to delete: ")
        user_info['tasks'].remove(select_task)  
        print("task has been deleted")   
