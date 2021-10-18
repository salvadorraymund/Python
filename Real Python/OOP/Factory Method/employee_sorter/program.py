import employees_sorter
import employees

my_trader = employees.Employee(1, 'Raymund', 'Global Trading')
my_sorter = employees_sorter.EmployeeSorter()
print(my_sorter.sort(my_trader, 'Global Trading'))
my_analyst = employees.Employee(2, 'Raymund', 'PTD')
print(my_sorter.sort(my_analyst, 'PTD'))
