import streamlit as st
import altair as alt
import pandas as pd
import requests
from bs4 import BeautifulSoup

import engine

engine.page_header()

engine.get_composite()

with st.container():
    cols = st.columns(2)
    with cols[0]:
        engine.top_5()
    with cols[1]:
        engine.low_5()

