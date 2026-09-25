"""
Streamlit page for playing a dice game.

Allows a player to select an opponent and play a game of dice.

Endpoints used:
    GET /player
    POST /game
"""

import streamlit as st

from utils.api_client import api_client
from utils.log_init import get_page_logger

st.title("Player stats")
logger = get_page_logger("player_stats")
idplayer = st.query_params.get("id_player")

if idplayer is not None:
    try:
        idplayer = int(idplayer)
        response = api_client.get(f"/player/{idplayer}")
        if response["status_code"] == 200:
            player = response["data"]
            st.subheader(f"{player['username']}")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Classement Elo", value=f"{player['elo']}")
            with col2:
                st.write(f"Email : {player['email']}")
                st.checkbox("Pokemon fan :", value=f"{player['pokemon_fan']}")

        st.divider()
        st.subheader("Historique")
        game_response = api_client.get(
            "/game",
            params={
                "id_player": idplayer,
                "game_mode": None,
            },
        )
        if game_response["status_code"] == 200:
            games = game_response["data"]
            if not games:
                st.info("Ce joueur n'a pas joué")
            else:
                for g in games:
                    player1 = g["player1"]
                    player2 = g["player2"]
                    winner = g["winner"]
                    opponent = None
                    result = None
                    if player1["id_player"] == idplayer:
                        opponent = player2
                    else:
                        opponent = player1
                    if winner:
                        if winner["id_player"] == idplayer:
                            result = "Win"
                        else:
                            result = "Loss"
                    else:
                        result = "Draw"
                    
        else:
            st.info("Echec de l'appel api games")
    except OSError:
        print("Le joueur est introuvable")
