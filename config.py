# import modules
import pandas as pd
import numpy as np
import datetime
import streamlit as st
from fbprophet.plot import plot_plotly
from fbprophet import Prophet


# set password that will be used for the application
app_password = 'kpi2020'

# set file name for client
<<<<<<< HEAD
client_file = "KPI DashboardBaptist.xlsx"
=======
client_file = 'KPI DashboardBaptist.xlsx'
>>>>>>> e65f119a81c61da78b4ca33a99bc46f6be3b6091
sheet = 'Weekly'

class Forecast():

    """ 
    This is a class performing a forecast on kpi data 
      
    Attributes: 
        kpi_data : filepath

    """

    def __init__(self, kpi_data):

        """ 
        The constructor for Forecast class. 
  
        Parameters: 
            kpi_data : filepath 
        """

        # get data
        self.data = kpi_data
        
        # column cleaning
        name_cols = ['Facility','KPI', 'Category']
        date_cols = self.data.columns.to_list()[3:]
        date_info = [f"{date.month}/{date.day}/{date.year}" for date in date_cols]
        all_cols = name_cols + date_info

        # update dataframe
        self.data.columns = all_cols

        # drop last datecolumn
        self.data = self.data.loc[:,['Facility',
        'KPI',
        'Category',
        '3/16/2020',
        '3/23/2020',
        '3/30/2020',
        '4/6/2020',
        '4/13/2020',
        '4/20/2020',
        '4/27/2020',
        '5/4/2020',
        '5/11/2020',
        '5/18/2020',
        '5/25/2020',
        '6/1/2020',
        '6/8/2020',
        '6/15/2020',
        '6/22/2020',
        '6/29/2020']]

        # drop the na columns
        self.data.dropna(axis=0, inplace=True)
        
        # put facilities into context
        self.facility = sorted(list(set(self.data['Facility'])))

        # unpivot date columns
        self.data = pd.melt(self.data, id_vars=['Facility', 'KPI', 'Category'], value_vars=['3/16/2020',
                                                                        '3/23/2020',
                                                                        '3/30/2020',
                                                                        '4/6/2020',
                                                                        '4/13/2020',
                                                                        '4/20/2020',
                                                                        '4/27/2020',
                                                                        '5/4/2020',
                                                                        '5/11/2020',
                                                                        '5/18/2020',
                                                                        '5/25/2020',
                                                                        '6/1/2020',
                                                                        '6/8/2020',
                                                                        '6/15/2020',
                                                                        '6/22/2020',
                                                                        '6/29/2020'], var_name='Date', value_name='KPI Value')

        # convert column to datetime
        self.data['Date'] = pd.to_datetime(self.data['Date'], infer_datetime_format=True)

        # drop category columns
        self.data.drop('Category', axis=1, inplace=True)

    def GetData(self, facility=None, kpi=None):
        """ 
        The function to get all of the facility kpi data 
  
        Parameters: 
            facility (string): The facility from the streamlit facility selector
            kpi (string): The kpi (key performance indicator) for the streamlit kpi selector
          
        Returns: 
            all_data: all of the data for the selected facility and kpi
        """

        all_data = self.data.loc[(self.data['Facility'] == facility)
                                        & (self.data['KPI'] == kpi)]
        return all_data

    def GetKPIs(self, facility=None):
        """ 
        The function to get the unique kpis to build the drop down in the streamlit kpi selector
  
        Parameters: 
            facility (string): The facility from the streamlit facility selector
          
        Returns: 
            kpis: return a unique list of all the facility kpis
        """
        current_data = self.data.loc[self.data['Facility'] == facility, 'KPI']
        kpis = list(set(current_data))
        return kpis

    def PlotData(self):
        """ 
        The function forecast and plot the data for the selected kpi
  
        Parameters: 
            None
          
        Returns: 
            fig: returns the predicted plotly data
            
        """    
        # set side bar selections
        facility = st.sidebar.selectbox("Facility", self.facility)
        kpi = st.sidebar.selectbox("KPI", sorted(self.GetKPIs(facility=facility)))
            
        # set take for current facility
        st.title(f'{kpi} Forecasting For {facility}')
            
        # get facility kpi data
        facility_kpi_data = self.GetData(facility=facility, kpi=kpi)
            
        # get the data that is needed to model
        model_data = facility_kpi_data[['Date', 'KPI Value']]
            
        # rename the columns so that the data can be modeled
        model_data.columns = ['ds', 'y']

        # load prophet model and fit
        model = Prophet()
        model.fit(model_data)

        # set future dates
        future = model.make_future_dataframe(periods=12, freq='W')

        # forecast data
        forecast = model.predict(future)

        # Python
        fig = plot_plotly(model, forecast, ylabel=f'{kpi}', xlabel='Dates', figsize=(1000, 700))  # This returns a plotly Figure

        return fig

