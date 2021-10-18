# from roles import(
#     PG, SG, SF, PF, C)
# from skills import(PlayerSkill)

from college_directory import get_school_name
from roles import get_role
from skills import get_status


class _Player_Database:
    def __init__(self):
        self._ballers = {
            1: {
                'name': 'Raymund Salvador',
                'jersey_number': 31,
                'role': 'point_guard',
                'salary': 50000
            },
            2: {
                'name': 'Carmelo Anthony',
                'jersey_number': 35,
                'role': 'power_forward',
                'salary': 100000
            },
            3: {
                'name': 'Lebron James',
                'jersey_number': 23,
                'role': 'small_forward',
                'salary': 400000
            }
        }

    @property
    def ballers(self):
        return [Baller(id) for id in self._ballers]

    def get_baller_info(self, baller_id):
        info = self._ballers.get(baller_id)
        if not info:
            raise ValueError('Invalid baller_id')
        return info


class Baller:
    def __init__(self, id):
        self.id = id
        info = player_database.get_baller_info(self.id)
        self.name = info.get('name')
        self.jersey_number = info.get('jersey_number')
        self.school_name = get_school_name(self.id)
        self.role = get_role((info.get('role')))
        self.salary = info.get('salary')

    def player_status(self):
        status = get_status(self.salary)
        print(f'{self.name} ({self.school_name}) -- {status}')

    def __str__(self):
        return f'{self.name} hails from {self.school_name} and wears jersey number {self.jersey_number}.'


player_database = _Player_Database()


# class CreatePG(Baller, PG, PlayerSkill):
#     def __init__(self, name, jersey_number, college, salary):
#         PlayerSkill.__init__(self, salary)
#         super().__init__(name, jersey_number, college)

#     # def salary(self, salary):
#     #     self.salary = salary


# class CreateSG(Baller, SG, PlayerSkill):
#     def __init__(self, name, jersey_number, college, salary):
#         PlayerSkill.__init__(self, salary)
#         super().__init__(name, jersey_number, college)

#     # def salary(self, salary):
#     #     self.salary = salary


# class CreateSF(Baller, SF, PlayerSkill):
#     def __init__(self, name, jersey_number, college, salary):
#         PlayerSkill.__init__(self, salary)
#         super().__init__(name, jersey_number, college)

#     # def salary(self, salary):
#     #     self.salary = salary


# class CreatePF(Baller, PF, PlayerSkill):
#     def __init__(self, name, jersey_number, college, salary):
#         PlayerSkill.__init__(self, salary)
#         super().__init__(name, jersey_number, college)

#     # def salary(self, salary):
#     #     self.salary = salary


# class CreateC(Baller, C, PlayerSkill):
#     def __init__(self, name, jersey_number, college, salary):
#         PlayerSkill.__init__(self, salary)
#         super().__init__(name, jersey_number, college)

#     # def salary(self, salary):
#     #     self.salary = salary
