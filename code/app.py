import streamlit as st
import os
import session_state as ss
import pandas as pd
from config import Forecast, client_file, sheet

# set Forecast Class
forecast = Forecast(kpi_data=pd.read_excel(os.path.join('../data',client_file), sheet_name=sheet))

# set session password to blank
session_state = ss.get(password='')

# check to see if the session password is valid
if session_state.password != 'kpi2020':
    pwd_placeholder = st.empty()
    pwd = pwd_placeholder.text_input("Password:", value="", type="password")
    session_state.password = pwd
    if session_state.password == 'kpi2020':
        pwd_placeholder.empty()
        forecast = forecast.PlotData()
        forecast
    elif session_state.password == '':
        pass
    else:
        st.error("the password you entered is incorrect")
else:
    forecast = forecast.PlotData()
    forecast


