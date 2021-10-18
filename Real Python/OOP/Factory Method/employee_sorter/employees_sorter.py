import json


class EmployeeSorter:
    def sort(self, employee, department):
        employee_sorter = department_factory.get_department(department)
        employee.sort(employee_sorter)
        return employee_sorter.to_str()


class GlobalTrading:
    def __init__(self):
        self._trader = None

    def create_dictionary(self, object_name, object_id):
        self._trader = {
            'id': object_id
        }

    def add_key_value(self, name, value):
        self._trader[name] = value

    def to_str(self):
        return json.dumps(self._trader)

    # def __str__(self):
    #     return str(self._trader)

    def get_item(self, value):
        my_value = self._trader.get(value)
        return my_value


class PTD:
    def __init__(self):
        self._analyst = None

    def create_dictionary(self, object_name, object_id):
        self._analyst = {
            'id': object_id
        }

    def add_key_value(self, name, value):
        self._analyst[name] = value

    def to_str(self):
        return json.dumps(self._analyst)


class Logistics:
    def __init__(self):
        self._associate = None

    def create_dictionary(self, object_id, object_name):
        self._associate = {
            'id': object_id
        }

    def add_key_value(self, name, value):
        self._associate[name] = value

    def to_str(self):
        return json.dumps(self._associate)


class DepartmentRegistration:
    def __init__(self):
        self._departments = {}

    def register(self, department, deparment_class):
        self._departments[department] = deparment_class

    def get_department(self, department):
        assignment = self._departments.get(department)
        if not assignment:
            raise ValueError(department)
        return assignment()


department_factory = DepartmentRegistration()
department_factory.register("Global Trading", GlobalTrading)
department_factory.register("PTD", PTD)
department_factory.register("Logistics", Logistics)
# global_trader = GlobalTrading()
# global_trader.create_dictionary('id', 1)
# global_trader.add_key_value('name', 'Raymund')
# trader_name = global_trader.get_item('name')
# print(trader_name)
