# Import required packages/libraries [dash,finances,dataframe,plotting]
import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
#Adding datetime to filter by date
import datetime


analysis = st.sidebar.selectbox("Desplegable", ["Ibex35","SP500","CryptoUSD"])

if analysis == "Ibex35":


    st.write('---')
    #Section title
    st.markdown('''
    # Valor acciones IBEX35
    ''')
    st.write('---')

    # Date picker
    st.header('Selecciona valor')

    ticker_list=pd.read_csv('ibex35.txt')
    tickerSymbol=st.selectbox('Código bursátil', ticker_list)
    tickerData=yf.Ticker(tickerSymbol)
    #La fecha a seleccionar podemos ponerla en body o en la sidebar añadiendo stt.sidebar
    start_date=st.date_input("Fecha inicial", datetime.date(2021, 1, 1))
    end_date=st.date_input("Fecha final", datetime.date(2021, 3, 15))
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)
    string_logo = '<img src=%s>' % tickerData.info['logo_url']
    st.markdown(string_logo, unsafe_allow_html=True)

    st.header('**Representación sencilla del valor seleccionado**')
    tickercopyDf=tickerDf
    tickercopyDf=tickercopyDf.drop(['Volume', 'Dividends','Stock Splits'], axis=1)
    st.line_chart(tickercopyDf,use_container_width=True)


    st.header('**Tabla/DF del valor seleccionado**')
    st.write(tickerDf)

    #Bollinger bands
    st.header('**Bandas de Bollinger**')
    qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
    qf.add_sma([10,20],width=2,color=['green','lightgreen'],legendgroup=True)
    qf.add_rsi(periods=20,color='java')
    qf.add_bollinger_bands(periods=20,boll_std=2,colors=['magenta','grey'],fill=True)
    qf.add_volume()
    qf.add_macd()
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)


elif analysis == "SP500":

    st.write('---')
    #Section title
    st.markdown('''
    # Valor acciones SP500
    ''')
    st.write('---')

    # Date picker
    st.header('Selecciona valor')

    ticker_list2=pd.read_csv('sp500.txt')
    tickerSymbol2=st.selectbox('Código bursátil', ticker_list2)
    tickerData2=yf.Ticker(tickerSymbol2)
    #La fecha a seleccionar podemos ponerla en body o en la sidebar añadiendo stt.sidebar
    start_date2=st.date_input("Fecha inicial", datetime.date(2021, 1, 1))
    end_date2=st.date_input("Fecha final", datetime.date(2021, 3, 15))
    tickerDf2 = tickerData2.history(period='1d', start=start_date2, end=end_date2)
    string_logo2 = '<img src=%s>' % tickerData2.info['logo_url']
    st.markdown(string_logo2, unsafe_allow_html=True)

    st.header('**Representación sencilla del valor seleccionado**')
    tickercopyDf2=tickerDf2
    tickercopyDf2=tickercopyDf2.drop(['Volume', 'Dividends','Stock Splits'], axis=1)
    st.line_chart(tickercopyDf2,use_container_width=True)

    st.header('**Tabla/DF del valor seleccionado**')
    st.write(tickerDf2)

    #Bollinger bands
    st.header('**Bandas de Bollinger**')
    qf=cf.QuantFig(tickerDf2,title='First Quant Figure',legend='top',name='GS')
    qf.add_sma([10,20],width=2,color=['green','lightgreen'],legendgroup=True)
    qf.add_rsi(periods=20,color='java')
    qf.add_bollinger_bands(periods=20,boll_std=2,colors=['magenta','grey'],fill=True)
    qf.add_volume()
    qf.add_macd()
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)
    
elif analysis == "CryptoUSD":


    st.write('---')
    #Section title
    st.markdown('''
    # Valor en USD de diversas cryptomonedas
    ''')
    st.write('---')

    # Date picker
    st.header('Selecciona valor')

    ticker_list3=pd.read_csv('crypto.txt')
    tickerSymbol32=st.selectbox('Denominación de la cryptomoneda', ticker_list3)
    tickerData3=yf.Ticker(tickerSymbol3)
    #La fecha a seleccionar podemos ponerla en body o en la sidebar añadiendo stt.sidebar
    start_date3=st.date_input("Fecha inicial", datetime3.date(2021, 1, 1))
    end_date3=st.date_input("Fecha final", datetime3.date(2021, 3, 15))
    tickerDf3 = tickerData3.history(period='1d', start=start_date3, end=end_date3)
    string_logo3 = '<img src=%s>' % tickerData3.info['logo_url']
    st.markdown(string_logo3, unsafe_allow_html=True)

    st.header('**Representación sencilla del valor seleccionado**')
    tickercopyDf3=tickerDf3
    tickercopyDf3=tickercopyDf3.drop(['Volume', 'Dividends','Stock Splits'], axis=1)
    st.line_chart(tickercopyDf3,use_container_width=True)

    st.header('**Tabla/DF del valor seleccionado**')
    st.write(tickerDf3)


