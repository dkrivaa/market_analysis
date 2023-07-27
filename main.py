import streamlit as st
import altair as alt
import pandas as pd
import requests
from bs4 import BeautifulSoup

import engine

st.write(engine.get_data())

