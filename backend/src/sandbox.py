from business_object.player import Player
from dao.game_dao import GameDao
from service.game_service import GameService
from utils.env_variables import display_values, load_environment_variables
from utils.log_utils import initialize_logs

# Initialization
initialize_logs("Webservice")

load_environment_variables()
display_values()


g = GameService().play(3, 5, "coinflip", choice="tails")
print(g)

print(f"{g.player1.username} : new elo -> {g.player1.elo}")
print(f"{g.player2.username} : new elo -> {g.player2.elo}")

g2 = GameService().play(3, 5, "dice")
print(g2)

print(f"{g2.player1.username} : new elo -> {g2.player1.elo}")
print(f"{g2.player2.username} : new elo -> {g2.player2.elo}")

created_game = GameDao().create(g)
player1 = Player("batricia", 1342, "bat.project.io")
player1.id_player = 3
list = GameDao().find_all_by_player(player1)
for game in list:
    print(game)
