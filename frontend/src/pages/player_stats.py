"""
Streamlit page for recuperating player stats.
.

Endpoints used:
    GET /player
    POST /game
"""

import streamlit as st

from utils.api_client import api_client
from utils.log_init import get_page_logger

st.title("Player Statistics")
logger = get_page_logger("player_stats")
identifiant = int(st.query_params.get("id_player"))

response = api_client.get(f"/player/{identifiant}")

if response["status_code"] != 200:
    st.error(response["data"])
    st.stop()

data = response["data"]
st.write(f"**{data['username']}**")
st.write(f"**{data['elo']}**")
st.write(f"**{data['email']}**")
st.write(f"** Pokemon fan : {data['description']}**")
