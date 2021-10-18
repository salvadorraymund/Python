# import baller
# import roles
# import skills

# one = baller.CreatePG('Raymund', 4, 'Duke', 50000)
# two = baller.CreatePF('Melo', 1, 'Chino Hills', 250000)
# three = baller.CreateSG('Gelo', 0, 'UCLA', 100000)

# players = [one, two, three]
# lineup = roles.Roster()
# player_positions = lineup.roles(players)

# # player_one_salary = one.salary(50000)
# # player_two_salary = two.salary(250000)
# # player_three_salary = three.salary(100000)
# # players_salary = [(one.salary(50000)), (two.salary(450000)),
# #                   (three.salary(100000))]
# player_status = skills.PlayerStatus()
# skill_level = player_status.skill_level(players)
# # print(dir(player_three_salary))

from baller import player_database, Baller
from roles import roles
from skills import get_skill_level

players = player_database.ballers
roles(players)
get_skill_level(players)
