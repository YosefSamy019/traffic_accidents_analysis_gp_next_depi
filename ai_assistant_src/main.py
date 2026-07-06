import streamlit as st

from functions import clear_msgs_buffer
from models.models import AgentStatus
from values.const import AGENT_STATUS
from view.agent_loop import is_goal_achieved, call_model, mark_expired_msgs
from view.chat_view import build_chat, build_messages
from view.init_view import init
from view.sidebar_view import build_sidebar

import tools.execute_sql_tool as _


def main():
    init()
    build_sidebar(
        clear_chat_func=clear_msgs_buffer
    )
    build_chat()
    build_messages()

    if is_goal_achieved() and st.session_state[AGENT_STATUS] == AgentStatus.RUNNING:
        st.session_state[AGENT_STATUS] = AgentStatus.STOPPED
        st.rerun()

    if st.session_state.get(AGENT_STATUS) == AgentStatus.RUNNING:
        call_model()
        mark_expired_msgs()
        st.rerun()


if __name__ == "__main__":
    main()
