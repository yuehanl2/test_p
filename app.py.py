# Mini assignment BY @YUEHAN LAN

import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from vega_datasets import data

counties = alt.topo_feature(data.us_10m.url, 'counties')
source = data.unemployment.url
df_rates=pd.read_csv(source, delimiter='\t')
rate_emp=pd.read_csv(source, delimiter='\t')

#st.write(df_rates)


# The rate of df_rates also weill be 1-rate. why?
#rate_emp = df_rates
rate_emp['rate'] = 1-rate_emp['rate']

#st.write(rate_emp)




radioButton = st.radio(
     "What do you want to show?",
     ('rate', 'rare_emp'))

if radioButton == 'rate':
    st.write('Unemployment Rate')
    ch_map = alt.Chart(counties).mark_geoshape().encode(
        color='rate:Q',
        tooltip=['id:O', 'rate:Q']
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(df_rates, 'id', ['rate'])
    ).project(
        type='albersUsa'
    ).properties(
        width=600,
        height=400
    )
    ch_map
else:
    st.write("Employment Rate")
    ch_map = alt.Chart(counties).mark_geoshape().encode(
        color='rate:Q',
        tooltip=['id:O', 'rate:Q']
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(rate_emp, 'id', ['rate'])
    ).project(
        type='albersUsa'
    ).properties(
        width=600,
        height=400
    )
    ch_map


