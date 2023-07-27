import streamlit as st
import altair as alt
import pandas as pd
import requests
from bs4 import BeautifulSoup

import engine

engine.page_header()

st.write(engine.get_composite())

