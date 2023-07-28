import streamlit as st

import engine


engine.page_header()

with st.container():
    cols = st.columns(2)
    with cols[0]:
        engine.top_5()
    with cols[1]:
        engine.low_5()

