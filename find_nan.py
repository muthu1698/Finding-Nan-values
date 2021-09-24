import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import os
import io
import base64


# Uploading files
st.title("Here you can Upload One File at a Time")
d = st.file_uploader("Upload a file", type=["xlsx"])




# loading the data
data = pd.read_excel(d)
st.header('Your DataSet')


# To highlight the nan value in the data
#st.write('The nan value will be Highlighted in the table.')
#color = data.style.applymap(lambda x: 'color: red' if pd.isnull(x) else '')
#color

st.write('Total number of sheets found in a single file')
xls = pd.ExcelFile(d)
ss = xls.sheet_names
ss


for sheet_name in ss:
    print(sheet_name)
    xyz = pd.read_excel(d, sheet_name=sheet_name, index_col=None)
    thor = xyz
    thor



# To find the null value in a single file
st.header('The total Nan value count in the data')
df1 = data.isnull().sum().sum()
st.write("The Total Number of Nan value Present in the DataSet is:",df1)

# To show which column have the nan value in it
st.header('Display Nan value')
st.write('Full report here the nan value are present in the data.')
dff = data[data.isna().any(axis=1)]
color = dff.style.applymap(lambda x: 'color: red' if pd.isnull(x) else '')
color
st.write('----')


st.title("Here you can Upload Multiple file")

# To uploaded multiple file
uploaded_files = st.file_uploader("Upload exels", type="xlsx", accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        file.seek(0)
    uploaded_data_read = [pd.read_excel(file) for file in uploaded_files]
    raw_data = pd.concat(uploaded_data_read, join='outer', axis=1)
    final_file = raw_data.loc[:, ~raw_data.columns.duplicated()]



st.write("Your Final Combined DataSet")
# To highlight the nan value in the data
color = final_file.style.applymap(lambda x: 'color: red' if pd.isnull(x) else '')
color

# To find the null value in a single file
st.header('The total Nan value count in the data')
comb_df1 = final_file.isnull().sum().sum()
st.write("The Total Number of Nan value Present in the DataSet is:",comb_df1)

# To show which column have the nan value in it
st.header('Display Nan value')
st.write('Full report here the nan value are present in the data.')
comb_dff = comb_df1[comb_df1.isna().any(axis=1)]
color = comb_dff.style.applymap(lambda x: 'color: red' if pd.isnull(x) else '')
color
st.write('----')
