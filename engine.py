# THIS IS THE FILE OF ALL THE FUNCTIONS USED IN THIS APP

import streamlit as st
import altair as alt
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import datetime


# LAYOUT

def page_header():
    # Function for page header
    st.set_page_config(page_title='Nasdaq Stock Market')

    url = 'data:image/png;base64,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'
    st.image(url)
    st.write(datetime.date.today().strftime("%d %B %Y"))
    get_composite()
    st.markdown('___')


# DATA


def get_composite():
    # Function to get the latest data on Nasdaq Composite
    url = 'https://www.investing.com/indices/nasdaq-composite'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        latest = soup.find('div', class_='text-5xl font-bold leading-9 md:text-[42px] md:leading-[60px] text-[#232526]')
        absolute_change = soup.find('div', class_='text-base font-bold leading-6 md:text-xl md:leading-7 rtl:force-ltr')
        prev_close = soup.find('span', class_='key-info_dd-numeric__ZQFIs')
    if latest is not None:
        latest_composite = latest.text
    if absolute_change is not None:
        latest_abs_change = absolute_change.text
    if prev_close is not None:
        previous_close = prev_close.text

    return st.metric('Nasdaq Composite', value=latest_composite, delta=latest_abs_change)


def get_data():
    # Function to get stock data
    url = 'https://stockanalysis.com/api/screener/s/f?m=marketCap&s=desc&c=no,s,n,marketCap,price,change,revenue,volume,industry,sector,revenueGrowth,netIncome,fcf,netCash&cn=0&f=exchange-is-NASDAQ&p=2&dd=true&i=allstocks'
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data
        stock_data = json.loads(response.text)
    # Extract data
    nested_data = stock_data['data']['data']
    # Making dataframe with all stock data
    df = pd.DataFrame(nested_data)
    df = df.rename(columns={'s': 'symbol', 'n': 'company name',
                            'fcf': 'free_cash_flow', 'netCash': 'net_cash_debt'})
    df.drop('no', axis=1, inplace=True)
    return df


def sector():
    df = get_data()
    df = df.groupby(df['sector'])['change'].mean()
    # x_list = []
    # for i in range(0, len(df)):
    #     x = float(df.iloc[i])
    #     x_list.append(x)
    # y_list = df.axes
    df = pd.Series(df)
    df = df.reset_index()
    df.columns = ['sector', 'value']
    df['value'] = df['value']/100
    df['color'] = df['value'].apply(lambda x: '#D51A05' if x < 0 else '#56BF11')
    c = alt.Chart(df).mark_bar().encode(
        x=alt.X('value', axis=alt.Axis(format='%')),
        y=alt.Y('sector').sort('-x'),
        color=alt.Color('color:N', scale=None)
    )
    st.altair_chart(c)


def big_10():
    # Function to get chart of change of big 10
    df = get_data()
    big_10 = df.nlargest(10, 'marketCap')
    big_10['change'] = big_10['change']/100
    big_10['color'] = big_10['change'].apply(lambda x: '#D51A05' if x < 0 else '#56BF11')
    c = alt.Chart(big_10).mark_bar().encode(
        x=alt.X('change', axis=alt.Axis(format='%')),
        y=alt.Y('company name').sort('-x'),
        color=alt.Color('color:N', scale=None)
    ).properties(
        title={
                'text': 'BIG 10',
                'fontSize': 25,
            }
    )

    st.altair_chart(c)

def top_5():
    # Function to get top 5 movers of the day
    df = get_data()
    top_5 = df.nlargest(5, 'change', )
    for i in range(0, len(top_5)):
        calc = float(top_5.iloc[i]['change']) / 100
        chg = f'{calc:.2%}'
        name = top_5.iloc[i]['company name']
        st.metric(name,
                  value=top_5.iloc[i]['price'],
                  delta=chg)

def low_5():
    # Function to get bottom 5 movers of the day
    df = get_data()
    low_5 = df.nsmallest(5, 'change', )
    for i in range(0, len(low_5)):
        calc = float(low_5.iloc[i]['change']) / 100
        chg = f'{calc:.2%}'
        name = low_5.iloc[i]['company name']
        st.metric(name,
                  value=low_5.iloc[i]['price'],
                  delta=chg)


def ticker():
    df = get_data()
    st.markdown(f'<span style="color: #18448c; font-size: 22px"><b>Choose Ticker/Company</b></span>'
                , unsafe_allow_html=True)

    def get_data_ticker():
        company = df.loc[df['symbol'] == st.session_state.ticker]
        if 'company' not in st.session_state:
            st.session_state.company = company
        else:
            st.session_state.company = company
        st.session_state.name = ((st.session_state.company['company name']).tolist())[0]

    def get_data_name():
        company = df.loc[df['company name'] == st.session_state.name]
        if 'company' not in st.session_state:
            st.session_state.company = company
        else:
            st.session_state.company = company
        st.session_state.ticker = ((st.session_state.company['symbol']).tolist())[0]


    with st.container():
        cols = st.columns(2)
        with cols[0]:
            ticker = st.selectbox('Choose Ticker', options=df['symbol'],
                                  key='ticker', on_change=get_data_ticker)

        with cols[1]:
            name = st.selectbox('Choose Company', options=df['company name'],
                                key='name', on_change=get_data_name)

    st.markdown('___')

    with st.container():
        if 'company' in st.session_state:
            cols = st.columns([1, 3])

            with cols[0]:
                cname = ((st.session_state.company['company name']).tolist())[0]
                price = float(st.session_state.company['price'])
                calc = float(st.session_state.company['change']) / 100
                chg = f'{calc:.2%}'
                st.write('latest data:')
                st.metric(f"{cname}",
                          value=f"{price}",
                          delta=f"{chg}")


            with cols[1]:
                # Getting 1-year data for chosen company
                url = 'https://stockanalysis.com/api/charts/s/' + str(st.session_state.ticker) + '/1Y/l'

                response = requests.get(url)
                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Parse the JSON data
                    company_data = json.loads(response.text)
                # Extract data
                nested_data = company_data['data']
                # Making dataframe with all stock data
                dfc = pd.DataFrame(nested_data)
                dfc.drop('o', axis=1, inplace=True)
                dfc['t'] = pd.to_datetime(dfc['t'], unit='s')
                dfc['t'] = dfc['t'].dt.date

                if dfc.loc[0, 'c'] < dfc['c'].iloc[-1]:
                    color = '#419C26'
                else:
                    color = '#9C3426'

                c = alt.Chart(dfc, title='Last 12 Months').mark_line(color=color).encode(
                    x=alt.X('t:T', title='Date', ),
                    y=alt.Y('c:Q', title='Stock Price'),
                )
                st.altair_chart(c)






