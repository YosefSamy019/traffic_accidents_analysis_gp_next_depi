from typing import List

import streamlit as st

from models.models import ChatMsg
from values.const import MSGS_KEY
from values.sys_prompt import get_sys_prompt


def clear_msgs_buffer():
    st.session_state[MSGS_KEY] = [
        get_sys_prompt()
    ]


def get_active_chat_msgs() -> List[ChatMsg]:
    return list(
        filter(
            lambda msg: msg.expired == False,
            st.session_state[MSGS_KEY]
        )
    )
