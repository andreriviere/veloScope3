from business_object.game import Game
from business_object.player import Player
from dao.db_connection import DBConnection
from dao.player_dao import PlayerDao
from utils.log_utils import get_logger, log
from utils.singleton import Singleton

logger = get_logger(__name__)


class GameDao(metaclass=Singleton):
    """Class containing methods to access Players in the database."""

    @log
    def create(self, game) -> bool:
        """Create a player in the database.
        Args:
            Player to create
        Returns:
            True if creation is successful, False otherwise
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO game(id_player1, id_player2, game_mode, id_winner, detail) VALUES "
                        "(%(id_player1)s, %(id_player2)s, %(game_mode)s, %(id_winner)s, %(detail)s) "
                        "RETURNING id_game;",
                        {
                            "id_player1": game.player1.id_player,
                            "id_player2": game.player2.id_player,
                            "game_mode": game.game_mode,
                            "id_winner": game.winner.id_player,
                            "detail": game.description,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        created = False
        if res:
            game.id_game = res["id_game"]
            created = True

        return created

    @log
    def find_by_id(self, id_game: int) -> Game:
        """Find a player by their id.
        Args:
            id_player (int): The ID of the player to find
        Returns:
            Player matching the given id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                            "
                        "  FROM game                       "
                        " WHERE id_game = %(id_game)s;   ",
                        {"id_game": id_game},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        game = None
        if res:
            p1 = PlayerDao().find_by_id(res["id_player1"])
            p2 = PlayerDao().find_by_id(res["id_player2"])
            winner = PlayerDao().find_by_id(res["id_winner"])
            game = Game(
                id_game=res["id_game"],
                player1=p1,
                player2=p2,
                game_mode=res["game_mode"],
                winner=winner,
                detail=res["detail"],
                timestamp=res["timestamp"],
            )

        return game

    @log
    def find_all_by_player(self, player: Player) -> list[Game]:
        """Find a player by their id.
        Args:
            id_player (int): The ID of the player to find
        Returns:
            Player matching the given id
        """
        print(player.id_player)
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT g.id_game, g.id_player1, g.id_player2, g.game_mode, g.id_winner, g.detail, g.timestamp "
                        "  FROM game g JOIN player p                      "
                        " ON p.id_player = g.id_player1 "
                        "  OR p.id_player = g.id_player2 "
                        " WHERE p.id_player = %(id_player)s;   ",
                        {"id_player": player.id_player},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise
        games_list = []
        print("coucouPremier")
        if res:
            print("coucou")
            for row in res:
                print("recoucou")
                p1 = PlayerDao().find_by_id(int(row["id_player1"]))
                p2 = PlayerDao().find_by_id(int(row["id_player2"]))
                winner = PlayerDao().find_by_id(int(row["id_winner"]))
                game = Game(
                    id_game=res["id_game"],
                    player1=p1,
                    player2=p2,
                    game_mode=res["game_mode"],
                    winner=winner,
                    detail=res["detail"],
                    timestamp=res["timestamp"],
                )
                games_list.append(game)
                print(len(games_list))
        return games_list

    @log
    def find_all(self) -> list[Game]:
        """List all players in the database.
        Returns:
            list[Player] sorted by username
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                "
                        "  FROM game                           "
                        " ORDER BY id_game;                     "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logger.error(e)
            raise

        games_list = []

        if res:
            for row in res:
                p1 = PlayerDao().find_by_id(row["id_player1"])
                p2 = PlayerDao().find_by_id(row["id_player2"])
                winner = PlayerDao().find_by_id(row["id_winner"])
                game = Game(
                    id_game=row["id_game"],
                    player1=p1,
                    player2=p2,
                    game_mode=row["game_mode"],
                    winner=winner,
                    detail=res["detail"],
                    timestamp=row["timestamp"],
                )

                games_list.append(game)

        return games_list

    @log
    def update(self, game) -> bool:
        """Update a game in the database.
        Args:
            Player to be updated
        Returns:
            True if update is successful, False otherwise
        """
        nb_affected_rows = 0

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE game                                                  "
                        "   SET id_player1 = %(id_player1)s,                                "
                        "       id_player2 = %(id_player2)s,            "
                        "       game_mode = %(game_mode)s,                                          "
                        "       id_winner = %(id_winner)s,                                      "
                        "       detail = %(detail)s,                          "
                        "       timestamp = %(timestamp)s,                          "
                        " WHERE id_game = %(id_game)s;                              ",
                        {
                            "id_game": game.id_game,
                            "id_player1": game.player1.id_player,
                            "id_player2": game.player2.id_player,
                            "game_mode": game.game_mode,
                            "id_winner": game.winner.id_player,
                            "detail": game.detail,
                            "timestamp": game.timestamp,
                        },
                    )
                    nb_affected_rows = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise

        return nb_affected_rows == 1

    @log
    def delete(self, game) -> bool:
        """Delete a player from the database.
        Args:
            Player to delete from the database
        Returns:
            True if the player was successfully deleted, False otherwise
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM game                               "
                        " WHERE id_game = %(id_game)s                 ",
                        {"id_game": game.id_game},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise

        return res > 0
