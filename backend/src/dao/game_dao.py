from business_object.game import Game
from dao.db_connection import DBConnection
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
                            "id_player1": game.id_player1,
                            "id_player2": game.id_player2,
                            "game_mode": game.game_mode,
                            "id_winner": game.id_winner,
                            "detail": game.detail,
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
            game = Game(
                id_player1=res["id_player1"],
                id_player2=res["id_player2"],
                game_mode=res["game_mode"],
                id_winner=res["id_winner"],
                detail=res["detail"],
            )

        return game

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
                game = Game(
                    id_player1=res["id_player1"],
                    id_player2=res["id_player2"],
                    game_mode=res["game_mode"],
                    id_winner=res["id_winner"],
                    detail=res["detail"],
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
                            "id_player1": game.id_player1,
                            "id_player2": game.id_player2,
                            "game_mode": game.game_mode,
                            "id_winner": game.id_winner,
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
