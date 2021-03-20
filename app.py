# Import required packages/libraries [dash,finances,dataframe,plotting]
import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
#Adding datetime to filter by date
import datetime

st.write('---')
#App title
st.markdown('''
# Valor acciones SP500
''')
st.write('---')

# Sidebar
st.sidebar.header('Selecciona valor')

ticker_list=pd.read_csv('iniciales.txt')
tickerSymbol=st.sidebar.selectbox('Código bursátil', ticker_list)
tickerData=yf.Ticker(tickerSymbol)
#La fecha a seleccionar podemos ponerla en body o en la sidebar añadiendo stt.sidebar
start_date=st.date_input("Fecha inicial", datetime.date(2021, 1, 1))
end_date=st.date_input("Fecha final", datetime.date(2021, 3, 15))
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.sidebar.markdown(string_logo, unsafe_allow_html=True)



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


#Adding the full name of the picked ticker
#string_name=tickerData.info['longName']
#st.header('**%s**'%string_name)
#string_summary=tickerData.info['longBusinessSummary']
#st.info(string_summary)
