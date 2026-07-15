import streamlit as st

from models.models import AgentStatus
from values.const import *
from values.sys_prompt import get_sys_prompt


def init():
    st.set_page_config(
        page_title="My Simple Coder Agent 🤖",
        layout="wide",
    )

    st.session_state.setdefault(API_KEY, '')
    st.session_state.setdefault(ERROR_MSG, '')
    st.session_state.setdefault(CALLS_COUNTER, 0)
    st.session_state.setdefault(AGENT_STATUS, AgentStatus.STOPPED)
    st.session_state.setdefault(MSGS_KEY, [
        get_sys_prompt()
    ])


