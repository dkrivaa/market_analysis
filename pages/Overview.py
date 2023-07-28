import streamlit as st

import engine


engine.page_header()

engine.sector()

with st.container():
    cols = st.columns(2)
    with cols[0]:
        st.markdown(f'<span style="color: #18448c; font-size: 14px"><b>Top 5</b></span>'
                    , unsafe_allow_html=True)
        engine.top_5()
    with cols[1]:
        st.markdown(f'<span style="color: #18448c; font-size: 14px"><b>Bottom 5</b></span>'
                    , unsafe_allow_html=True)
        engine.low_5()

