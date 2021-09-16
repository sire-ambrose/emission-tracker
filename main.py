import pandas as pd
import numpy as np
import streamlit as st
import joblib

st.write("# Annual CO2 Emission")


year=st.text_area(label='Year')
if st.button('Submit'):
    'You selected: ', year


'\n'

State = st.selectbox(
    'State',
     ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
       'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
       'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
       'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN',
       'TX', 'US-TOTAL', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'])

'You selected: ', State

'\n'

Producer_Type = st.selectbox(
    'Producer Type',
     ['Commercial Cogen', 'Commercial Non-Cogen', 'Electric Utility',
       'Industrial Cogen', 'Industrial Non-Cogen',
       'Total Electric Power Industry', 'IPP NAICS-22 Cogen',
       'IPP NAICS-22 Non-Cogen'])

'You selected: ', Producer_Type

'\n'

Energy_Source = st.selectbox(
    'Energy Source',
     ['All Sources', 'Coal', 'Petroleum', 'Natural Gas', 'Other',
       'Geothermal', 'Other Biomass', 'Wood and Wood Derived Fuels',
       'Other Gases'])

'You selected: ', Energy_Source

try:
    test= pd.DataFrame(data=[[int(year), State, Producer_Type, Energy_Source]],
    columns=['Year','State', 'Producer Type', 'Energy Source'])
    trans=joblib.load('trans.pkl')
    x=trans.transform(test)
    model=joblib.load('model.pkl')
    value= model.predict(x)
    'Predicted Value : ',abs(value[0])
except:
    pass



