class Employee:
    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department

    def sort(self, employee_sorter):
        employee_sorter.create_dictionary('id', self.employee_id)
        employee_sorter.add_key_value('name', self.name)
        employee_sorter.add_key_value('department', self.department)
