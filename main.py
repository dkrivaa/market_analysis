import streamlit as st
import altair as alt
import pandas as pd
import requests
from bs4 import BeautifulSoup

import engine

engine.page_header()

engine.get_composite()

engine.top_5()
engine.low_5()