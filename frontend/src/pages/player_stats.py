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
    except OSError:
        print("Le joueur est introuvable")
