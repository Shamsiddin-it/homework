from datetime import datetime

database=[]
users=[]
n=""
class User:
    id=0
    def __init__(self,first_name,last_name,email,username,password):
        self.id+=1
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.username=username
        self._password=password
        User.id+=1

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.username}"
class ManageUser:
    def registration(self):
        new_user = User(
            input("first_name: "),
            input("last_name: "),
            input("email: "),
            input("username: "),
            input("password: ")
        )
        users.append(new_user)

    def login(self,a,b):
        for user in users:
            if user.username==a and user._password==b:
                global n
                n = user.username
                return True
            else:
                return False

        
    def logout(self):
        pass


class Task(ManageUser):
    id=0 
    def __init__(self,task_name,due_date,description,user="",is_done=False):
        self.id+=1
        self.user = user
        self.task_name = task_name
        self.due_date = due_date
        self.description = description
        self.is_done = is_done
        self.created_at = datetime.now()
        Task.id+=1

    def __str__(self):
        return f"{self.user} {self.task_name} {self.due_date} {self.is_done}"
    
class TaskManager(ManageUser):
    def add_task(self):
        new_task = Task(
            input("Task name: "),
            input("Due date: "),
            input("Description: "),
            n
        )
        database.append(new_task)

    def get_task_by_id(self, id):
        for task in database:
            if task.id == id and task.user==n:
                return task
            
    def get_all_desk(self):
        for task in database:
            if task.user==n:
                print(task)

    def edit_task(self,id):
        task = self.get_task_by_id(id)
        task.task_name = input("Task_name: ")
        task.is_done = True
    
    def delete_task(self, id):
        task= self.get_task_by_id(id)
        database.remove(task)


user=ManageUser()
manager = TaskManager()
while True:
    us_input = input("reg or log or exit: ")
    if us_input=="reg":
        user.registration()
    elif us_input=="log":
        ht=user.login(input("Enter username: "),input("Enter password: "))
        if ht:
            while True:
                user_input = int(input("-> "))
                if user_input == 1:
                    manager.add_task()
                elif user_input == 2:
                    dr=manager.get_task_by_id(
                        int(input("Please enter task id to show: "))
                    )
                    print(dr)
                elif user_input == 3:
                    manager.get_all_desk()
                elif user_input == 4:
                    manager.edit_task(
                        int(input("Please enter task id to edit: "))
                    )
                elif user_input == 5:
                    manager.delete_task(
                        int(input("Please enter task id to delete: "))
                    )
                elif user_input == 6:
                    user.logout()
                    break
                else:
                    print("Please enter a number in range 1 to 6: ")
    elif us_input=="exit":
        print("You exit!")
        break



