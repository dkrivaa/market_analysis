import streamlit as st

import engine


engine.page_header()

# engine.ticker()

df = engine.get_data()
ticker = 'CSCO'
name = df.loc[df['symbol'] == ticker, df['company name']]
st.write(name)

