import streamlit as st
import pandas as pd

st.set_page_config("ICET College Information")
st.title('TELANGANA STATE COUNCIL OF HIGHER EDUCATION')
st.header('TSEAMCET - 2023')
# st.write('List of Colleges and Fee Details')
clg_info = pd.read_csv('pages/clg_info.csv')
new_columns = ['Institute Code', 'Institute Name', 'Place', 'Dist. Name', 'CollegeType',
               'Minority', 'Co-Educ.', 'Affil.to', 'BranchCode', 'fee', 'Convener Seats']
new_df = clg_info[new_columns].copy()
aff_clg = new_df['Affil.to'].unique()

st.write(f"The Engineering Colleges  are at {new_df['Place'].nunique()} different Places located in {new_df['Dist. Name'].nunique()} Districts of Telangana")
st.write(f"There are {new_df['Affil.to'].nunique()} Universities in Telangana")

aff = st.selectbox("Select University", [""] + list(aff_clg)) 
if aff !="":
    filtered_df = new_df[new_df['Affil.to'] == aff]
    # st.dataframe(filtered_df)
    sum_convener_seats = filtered_df['Convener Seats'].sum()
    st.info(f"studets will compete for {sum_convener_seats} seats to get into colleges that are Affiliated to {aff}")
    uf = filtered_df['Institute Name'].unique()
    st.success(f"Total colleges that are Affiliated to {aff} = {len(uf)}")
    st.dataframe(uf,width=950)
    st.warning(f"{aff} offers {filtered_df['BranchCode'].nunique()} Unique Engineering Cources")
    st.dataframe(filtered_df['BranchCode'].unique(),width = 200)
    min_fee = filtered_df['fee'].min()
    max_fee = filtered_df['fee'].max()
    if min_fee !=max_fee :
        st.warning(f"Fee range:  {min_fee} - {max_fee}")
    else :
        st.warning(f"Fee :  {min_fee} ")
    minority = filtered_df['Minority'].count()

    st.info(f"Number of branches in which Minorities can get advantage and get seat into =  {minority}")
    minority_filtered_df = new_df[(new_df['Affil.to'] == aff) & (new_df['Minority'].notna())]
    Minority_sum_convener_seats = minority_filtered_df['Convener Seats'].sum()
    st.success("Total Seats dedicated to Minorities = {} i.e {}% of total seats available".format(Minority_sum_convener_seats, round((Minority_sum_convener_seats/sum_convener_seats)*100)))

    clg = filtered_df['Institute Name'].unique()
    inst=st.selectbox("Explore College Wise",[""]+ list(clg))
    if inst !="":
        selec_inst = filtered_df[filtered_df['Institute Name'] == inst]
        st.success(f"Total Seates available  in {inst} = {selec_inst['Convener Seats'].sum()}")
        clg_min_fee = selec_inst['fee'].min()
        clg_max_fee = selec_inst['fee'].max()
        st.dataframe(selec_inst)
        if clg_min_fee != clg_max_fee :
            st.warning(f"Fee range:  {clg_min_fee} - {clg_max_fee}")
        else :
            st.warning(f"College Fee :  {clg_min_fee} ")
    
