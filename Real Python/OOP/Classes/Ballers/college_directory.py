class College:
    def __init__(self, school_name):
        self.school_name = school_name

    def __str__(self):
        return f'{self.school_name}'


class _College_Directory:
    def __init__(self):
        self.players_schools = {
            1: 'UP Diliman',
            2: 'Syracuse',
            3: 'St.Mary - St.Vincent'
        }

    def get_school_name(self, player_id):
        school_name = self.players_schools.get(player_id)
        if not school_name:
            raise ValueError('invalid player_id')
        return school_name


_college_directory = _College_Directory()


def get_school_name(player_id):
    return _college_directory.get_school_name(player_id)
