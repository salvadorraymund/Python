class _Roster:
    def __init__(self):
        self.roles = {
            'point_guard': PG,
            'shooting_guard': SG,
            'small_forward': SF,
            'power_forward': PF,
            'center': C
        }

    def get_role(self, role_id):
        role_type = self.roles.get(role_id)
        if not role_type:
            raise ValueError('invalid role_id')
        return role_type()

    def player_roles(self, players):
        print("LA Lakers 2021-2022 Roster")
        print("=================================")
        for player in players:
            print(f'{player.jersey_number} - {player.role.position()} - {player.name}')
        print('')


class PG:
    def position(self):
        return 'pointguard'

    def task(self):
        return f'create plays when in offense'


class SG:
    def position(self):
        return 'shooting guard'

    def task(self):
        return f'shoot perimeter shots'


class SF:
    def position(self):
        return 'small forward'

    def task(self):
        return f'shoot perimeter shots and be a tough defender'


class PF:
    def position(self):
        return 'power forward'

    def task(self):
        return f'shoot mid-range jumpers and rebound the ball'


class C:
    def position(self):
        return 'center'

    def task(self):
        return f'intimidate opposing teams shooting in the painted area and boxout'


_roster = _Roster()


def get_role(role_id):
    return _roster.get_role(role_id)


def roles(players):
    return _roster.player_roles(players)
