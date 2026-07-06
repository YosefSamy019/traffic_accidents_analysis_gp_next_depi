import streamlit as st

from models.models import ChatMsg
from values.const import MSGS_KEY


def add_message(msg: ChatMsg):
    st.session_state[MSGS_KEY].append(msg)
