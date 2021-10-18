# from abc import ABC, abstractmethod

# deriving from ABC tells users that you cannot instantiate new object to class Employee
# if they derive from the Employee class, they must override the method calculate_payroll

from hr import get_policy
from productivity import get_role
from contacts import get_employee_address
from representations import AsDictionaryMixin


# class Employee():
#     employee_count = 0

#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         self.address = None
#         if self.id == None:
#             try:
#                 Employee.employee_count += 1
#                 employee_id = "00" + str(Employee.employee_count)
#                 self.id = employee_id
#             except:
#                 raise KeyError("No id can be given")

# @abstractmethod
# the decorator @abstractmethod means that if you're deriving from Employee class,
# you must override the method calculate_payroll
# def calculate_payroll(self):
#     pass

class _EmployeeDatabase:
    def __init__(self):
        self._employees = {
            1: {
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            2: {
                'name': 'John Smith',
                'role': 'secretary'
            },
            3: {
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            4: {
                'name': 'Jane Doe',
                'role': 'factory'
            },
            5: {
                'name': 'Robin Williams',
                'role': 'secretary'
            }, }

    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError('invalid ID')
        return info


class Employee(AsDictionaryMixin):
    def __init__(self, id):
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get('name')
        self.address = get_employee_address(self.id)
        self._role = get_role(info.get('role'))
        self._payroll = get_policy(self.id)

    def work(self, hours):
        duties = self._role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()

    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy


employee_database = _EmployeeDatabase()

# class DisgruntledEmployee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def calculate_payroll(self):
#         return 10000


# class Manager(Employee, Manager, SalaryEmployee):
#     def __init__(self, id, name, weekly_salary):
#         SalaryEmployee.__init__(self, weekly_salary)
#         super().__init__(id, name)


# class Secretary(Employee, SecretaryRole, SalaryEmployee):
#     def __init__(self, name, id, weekly_salary):
#         SalaryEmployee.__init__(self, weekly_salary)
#         super().__init__(name, id)


# class SalesPerson(Employee, SalesPerson, CommissionEmployee):
#     def __init__(self, name, id, weekly_salary, commission):
#         CommissionEmployee.__init__(self, weekly_salary, commission)
#         super().__init__(name, id)


# class FactoryWorker(Employee, FactoryWorker, HourlyEmployee):
#     def __init__(self, name, id, hours_worked, hourly_rate):
#         super().__init__(name, id)
#         HourlyEmployee.__init__(self, hours_worked, hourly_rate)


# class TemporarySecretary(Employee, SecretaryRole, HourlyEmployee):
#     # The class TemporarySecretary is initialized with id, name, hours_worked, and hourly_rate
#     def __init__(self, id, name, hours_worked, hourly_rate):
#         # HourlyEmployee is called for hours_worked and hourly rate
#         HourlyEmployee.__init__(self, hours_worked, hourly_rate)
#         # Employee is called for id and name
#         super().__init__(id, name)


# MRO follows the order in the class arguments
# during initialization, order is not a problem
# you need to call super() to derive from Employee class
# print(FactoryWorker.__mro__)
