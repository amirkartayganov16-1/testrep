class Person:

    def __init__(self, username, salary):
        self.username = username
        self.salary = salary

    def info(self):
        print(f'username: {self.username}\n salary: {self.salary}')

    def change_salary(self, new_salary):
        self.new_salary = new_salary
        self.info()