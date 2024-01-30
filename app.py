import pandas as pd 
import numpy as np
import streamlit as st


st.set_page_config("Eamcet WebApp",page_icon="./logo.jpeg")
st.title("Eamcet Web Option Entry",anchor=False)
# Inputs to Take :
# Enter Rank
Rank = st.number_input("Enter Your Rank")
# Select PLACE
P = ['ABIDS','AGRAHARAM RAJANNA SIRCILLA','ARMOOR','BACHUPALLY','BANDLAGUDA','BATASINGARAM','BOWRAMPET','CHILKUR','CHOUTUPPAL','DESHMUKHI','DHULAPALLY','DUNDIGAL','GANDIPET','GHATKESAR','HANAMKONDA','HASANPARTHY','HAYATHNAGAR','HUZURABAD','HYDERABAD','IBRAHIMPATAN','IBRAHIMPATNAM','JAGITIAL','KACHIVANI SINGARAM','KACHWANISINGARA M','KAMAREDDY','KANDLAKOYA','KARIMNAGAR','KAZIPET','KEESARA','KHAMMAM','KODAD','KODADA','KOTHAGUDEM','KUKATPALLY','KUNTLOOR','MAHABUBNAGAR','MAISAMMAGUDA','MANTHANI','MASABTANK','MEDCHAL','MIRPET','MIRYALAGUDA','MIYAPUR','MOINABAD','MYSAMMAGUDA','NADERGUL','NAGOLE','NALGONDA','NARAYANAGUDA','NARSAMPET','NARSAPUR','NARSINGAYAPALLY VILLAGE','NIZAMABAD','PALONCHA','PARVATHAPUR','PATANCHERU','PEDDAPALLY','RUDRUR','SAIDABAD','SANGAREDDY','SATHUPALLY','SECUNDERABAD','SHAIKPET','SHAMSHABAD','SIDDIPET','SULTANPUR','SURYAPETA','WARANGAL','YENKAPALLY']
Place  = st.multiselect('Select Place',options=P)
Place=pd.Series(Place)
# Select University
U = ['ANURAG UNIVERSITY','CONSTITUENT COLLEGE','JNTUH','KU','MGUN','OU','PJTSAU','PVNRTVU','SR UNIVERSITY']
University = st.multiselect("Select University",options=U)
University = pd.Series(University)
# Select Branch
B = ['AERONAUTICAL ENGINEERING','AGRICULTURAL ENGINEERING','ARTIFICIAL INTELLIGENCE','ARTIFICIAL INTELLIGENCE AND DATA SCIENCE','ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING','AUTOMOBILE ENGINEERING','BIO-MEDICAL ENGINEERING','BIO-TECHNOLOGY','BTECH MECHANICAL WITH MTECH MANUFACTURING  SYSTEMS','BTECH MECHANICAL WITH MTECH THERMAL ENGG','CHEMICAL ENGINEERING','CIVIL ENGINEERING','COMPUTER ENGINEERING','COMPUTER ENGINEERING(SOFTWARE ENGINEERING)','COMPUTER SCIENCE & DESIGN','COMPUTER SCIENCE & ENGINEERING (NETWORKS)','COMPUTER SCIENCE AND BUSINESS SYSTEM','COMPUTER SCIENCE AND ENGINEERING','COMPUTER SCIENCE AND ENGINEERING\n(ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING)','COMPUTER SCIENCE AND ENGINEERING (CYBER SECURITY)','COMPUTER SCIENCE AND ENGINEERING (DATA SCIENCE)','COMPUTER SCIENCE AND ENGINEERING (IOT)','COMPUTER SCIENCE AND INFORMATION TECHNOLOGY','COMPUTER SCIENCE AND TECHNOLOGY','CSE (IoT AND CYBER SECURITY INCLUDING BLOCK CHAIN TECHNOLOGY)','DAIRYING','DIGITAL TECHNIQUES FOR DESIGN AND PLANNING','ELECTRICAL AND ELECTRONICS ENGINEERING','ELECTRONICS AND COMMUNICATION ENGINEERING','ELECTRONICS AND COMPUTER ENGINEERING','ELECTRONICS AND INSTRUMENTATION ENGINEERING','ELECTRONICS AND TELEMATICS','ELECTRONICS COMMUNICATION AND INSTRUMENTATION ENGINEERING','FACILITIES AND SERVICES PLANNING','FOOD TECHNOLOGY','INFORMATION TECHNOLOGY','MECHANICAL (MECHTRONICS) ENGINEERING','MECHANICAL ENGINEERING','METALLURGICAL ENGINEERING','METALLURGY AND MATERIAL ENGINEERING','MINING ENGINEERING','PHARMACEUTICAL ENGINEERING','PLANNING','TEXTILE TECHNOLOGY']
Branch = st.multiselect("Select Branch",options=B)
Branch=pd.Series(Branch)
# Cast :
C =['OC BOYS', 'OC GIRLS','BC_A BOYS', 'BC_A GIRLS', 'BC_B BOYS', 'BC_B GIRLS', 'BC_C BOYS','BC_C GIRLS', 'BC_D BOYS', 'BC_D GIRLS', 'BC_E BOYS', 'BC_E GIRLS','SC BOYS', 'SC GIRLS', 'ST BOYS', 'ST GIRLS', 'EWS GEN OU','EWS GIRLS OU']
cast = st.selectbox("Select Cast",options=C)
#-------------------
# Import Data Set:
df = pd.read_csv('EamcetDataSet2022.csv',index_col=False)
# st.dataframe(df)
# Define multiple criteria
c1 = df[cast] >= Rank
c2 = df['PLACE'].isin(Place)
c3 = df['AFFILIATED'].isin(University)
c4 = df['BRANCH NAME'].isin(Branch)
# Combine the criteria using logical operators
criteria_combined = c1 & c2 & c3 & c4
filtered_df = df[criteria_combined]
colList=['INST CODE', 'INSTITUTE NAME', 'PLACE', 'BRANCH', 'BRANCH NAME',cast,'TUITION FEE', 'AFFILIATED']
# Print the filtered DataFrame
fdf = filtered_df[colList]
st.dataframe(fdf)