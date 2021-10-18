from representations import AsDictionaryMixin


class _PayrollSystem(AsDictionaryMixin):
    # calculate_payroll is an interface to the PayrollSystem
    def __init__(self):
        self.employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    def get_policy(self, employee_id):
        policy = self.employee_policies.get(employee_id)
        if not policy:
            return ValueError(employee)
        return policy

    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('=================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'Check amount: {employee.calculate_payroll()}')
            if employee.address:
                print('--Sent to:')
                print(employee.address)
            print(' ')

    # def __str__(self):
    #     policy = self.employee_policies.get(employee_id)
    #     return f'{policy}'

class LTDPolicy:
    def __init__(self):
        self._base_policy = None
    def track_work(self, hours):
        self._check_base_policy()
        return self._base_policy.track_work(hours)
    def calculate_payroll(self):
        self._check_base_policy()
        base_salary = self._base_policy.calculate_payroll()
        return base_salary * 0.6
    def apply_to_policy(self, base_policy):
        self._base_policy = base_policy
    def _check_base_policy(self):
        if not self._base_policy:
            raise RunTimeError('Base policy missing!')

class Payroll_Policy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(Payroll_Policy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(Payroll_Policy):
    def __init__(self, hourly_rate):
        super().__init__()
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hourly_rate * self.hours_worked


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    def commission(self):
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        # instead of using the property weekly salary from the base, you just extended it by
        # assigning to variable fixed to avoid making changes when there's ammendment to the base
        fixed = super().calculate_payroll()
        return fixed + self.commission()


_payroll_system = _PayrollSystem()


def get_policy(employee_id):
    return _payroll_system.get_policy(employee_id)


def calculate_payroll(employees):
    return _payroll_system.calculate_payroll(employees)
