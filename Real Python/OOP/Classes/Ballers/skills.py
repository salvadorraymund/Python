class _PlayerStatus:
    def __init__(self):
        self.salary_level = {
            50000: Benchwarmer(),
            100000: Starter(),
            250000: AllStar(),
            400000: Superstar()
        }

    def get_status(self, salary):
        player_level = self.salary_level.get(salary)
        return player_level.ability()

    def skill_level(self, players):
        print("Player Status 2021-2022 Season")
        print("==============================")
        for player in players:
            player.player_status()
        print('')


class Benchwarmer:
    def ability(self):
        return "bench warmer"


class Starter:
    def ability(self):
        return "starter"


class AllStar:
    def ability(self):
        return "all star"


class Superstar:
    def ability(self):
        return "superstar"


_player_status = _PlayerStatus()


def get_status(salary):
    return _player_status.get_status(salary)


def get_skill_level(players):
    return _player_status.skill_level(players)
