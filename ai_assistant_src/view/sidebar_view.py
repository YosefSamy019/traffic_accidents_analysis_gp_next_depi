import streamlit as st

from logic.get_all_tools import get_all_tools_list
from values.const import *


def build_sidebar(
        clear_chat_func,
):
    with st.sidebar:
        st.title("⚙️ Settings")

        st.text_input(
            label="API KEY",
            key=API_KEY,
        )

        st.selectbox(
            label="Model",
            key=MODEL_KEY,
            index=0,
            options=VAL_MODELS
        )

        st.divider()

        if st.button("Clear Chat", width='stretch') and clear_chat_func:
            clear_chat_func()

        if st.button("Show Tools", width='stretch'):
            @st.dialog(title="Tools", width='large')
            def dialog():
                st.write(get_all_tools_list())

            dialog()

        if st.button("Show Buffer", width='stretch'):
            @st.dialog(title="Tools", width='large')
            def dialog():
                st.write([
                    m.to_json() for m in st.session_state.get(MSGS_KEY)
                ])

            dialog()
