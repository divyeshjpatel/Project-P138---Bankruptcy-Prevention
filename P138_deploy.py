import streamlit as st
import pickle

st.title("Bankruptcy Prevention Project")

st.info("Select values for each of the following features")

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

ind_risk = st.radio("1) Industrial Risk",("Low","Medium","High"))
man_risk = st.radio("2) Management Risk",("Low","Medium","High"))
fin_risk = st.radio("3) Financial flexibility",("Low","Medium","High"))
cre_risk = st.radio("4) Credibility",("Low","Medium","High"))
com_risk = st.radio("5) Competitiveness",("Low","Medium","High"))
ope_risk = st.radio("6) Operating Risk",("Low","Medium","High"))

risk = {'Low':0.0,'Medium':0.5,'High':1.0}

ind_risk = risk[ind_risk]
man_risk = risk[man_risk]
fin_risk = risk[fin_risk]
cre_risk = risk[cre_risk]
com_risk = risk[com_risk]
ope_risk = risk[ope_risk]

with open('P138_model' , 'rb') as file:
    model = pickle.load(file)
    
y = model.predict([[ind_risk, man_risk, fin_risk, cre_risk, com_risk, ope_risk]])

if y == 0:
    st.success("Company may not go bankrupt.")
else:
    st.warning("Company may go bankrupt.") 
