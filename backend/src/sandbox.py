from service.game_service import GameService
from utils.env_variables import display_values, load_environment_variables
from utils.log_utils import initialize_logs
from client.game_client import GameClient

# Initialization
initialize_logs("Webservice")

load_environment_variables()
display_values()

client = GameClient()
games = client.get_games()
print(f"{len(games)} games loaded:")
for g in games:
    print(f"- {g}")
