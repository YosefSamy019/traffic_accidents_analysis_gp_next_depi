from openai import OpenAI
import streamlit as st

from const import *

from values.const import *


def get_client() -> OpenAI:
    api = st.session_state[URL_KEY]
    endpoint = st.session_state[END_POINT_KEY]

    api = str(api).strip('/')
    endpoint = str(endpoint).strip('/')

    base_url = f"{api}/{endpoint}"

    client = OpenAI(
        base_url=base_url,
        api_key='<NOT_USED>'
    )

    return client
