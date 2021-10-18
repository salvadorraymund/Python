# import employee
# import hr
# import productivity
# import contacts

# manager = employee.Manager('Mary Poppins', None, 3000)
# manager.address = contacts.Address(
#     '121 Admin Rd',
#     'Concord',
#     'NH',
#     '03301')
# secretary = employee.Secretary('John Smith', None, 1500)
# secretary.address = contacts.Address(
#     '67 Paperwork Ave.',
#     'Manchester',
#     'NH',
#     '03101')
# sales_guy = employee.SalesPerson('Kevin Bacon', None, 1000, 250)
# factory_worker = employee.FactoryWorker('Jane Doe', None, 40, 15)
# temporary_secretary = employee.TemporarySecretary(
#     'Robin Williams', None, 40, 9)
# employees = [manager, secretary, sales_guy,
#              factory_worker, temporary_secretary]
# productivity_system = productivity.ProductivitySystem()
# productivity_system.track(employees, 40)
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(employees)
# In program.py

from hr import calculate_payroll, LTDPolicy
from productivity import track
from employee import employee_database, Employee
import json

# productivity_system = ProductivitySystem()
# payroll_system = PayrollSystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees
# manager = employees[0]
# manager.payroll = HourlyPolicy(55)
# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)


def print_dict(d):
    print(json.dumps(d, indent=2))


employees = employee_database.employees()

sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)

track(employees, 40)
calculate_payroll(employees)
