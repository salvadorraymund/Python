from representations import AsDictionaryMixin


class _ProductivitySystem(AsDictionaryMixin):
    def __init__(self):
        self.roles = {
            'manager': Manager,
            'secretary': SecretaryRole,
            'sales': SalesPerson,
            'factory': FactoryWorker
        }

    def get_role(self, role_id):
        role_type = self.roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type()

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('===========================')
        for employee in employees:
            employee.work(hours)
        print('')


class Manager:
    def perform_duties(self, hours):
        return f'screams and yells for {hours} hours.'


class SecretaryRole:
    def perform_duties(self, hours):
        return f'spends {hours} hours doing paperwork.'


class SalesPerson:
    def perform_duties(self, hours):
        return f'expends {hours} hours on the phone.'


class FactoryWorker:
    def perform_duties(self, hours):
        return f'manufactures gadgets for {hours} hours.'


# class TemporarySecretaryRole:
#     def __init__(self, name, id, hourly_rate, hours_worked):
#         HourlyEmployee.__init__(self, name, id, hourly_rate, hours_worked)

#     def calculate_payroll(self):
#         return HourlyEmployee.calculate_payroll(self)

_productivity_system = _ProductivitySystem()


def get_role(role_id):
    return _productivity_system.get_role(role_id)


def track(employees, hours):
    return _productivity_system.track(employees, hours)
