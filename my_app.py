import streamlit as st
import pickle
import numpy as np
from datetime import datetime

def days_xtract(input8,input9,input10):
        d1 = str(input8)
        d2 = str(input9)
        d3 = str(input10)

        d1 = datetime.strptime(d1, "%Y-%m-%d")
       
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        d3 = datetime.strptime(d3, "%Y-%m-%d")

        try:
            days_for_submit = d2 - d1
            days_for_submit = int(str(days_for_submit))
        except ValueError:
            days_for_submit = 0
            
        try:
            diff = d3 - d2
            diff = int(str(diff))
        except ValueError:
            diff = 0
        return days_for_submit,diff

def value_predictor(to_predict_list):
	to_predict = np.array(to_predict_list).reshape(1,13)
	loaded_model = pickle.load(open("model_pkl.pkl", "rb"))
	result = loaded_model.predict(to_predict)
	return result[0]

html_temp = """
<div style = "background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Procurement Fraud detection </h2>
</div>"""

def main():
    sub_cat = ['Juice','Crab','Yogurt','Sponges / Scrubbers','Broth','Burritos','Milk','Lobster','Butter / Margarine','Salmon','Applesauce','Cottage cheese','Air freshener','Vegetables','Catfish','Beer','Bleach / Detergent','Olives','Soda/Pop','Baked beans','Veggies','Shrimp','Wine','Garbage bags','Glass cleaner','Vacuum bags','Pizza','Breakfasts','Sports Drinks']
    st.title("Procurement Fraud Detection")
    st.markdown(html_temp,unsafe_allow_html=True)
    input1 = st.selectbox('Approving Officer Name',['name1','Name2','Name3'])
    input2 = st.selectbox('Requesting Officer Name',['Name1','Name2'])
    input3 = st.selectbox('Supplier Name',['Name1','Name2'])
    input4 = st.selectbox('Product Category',['category 1','Category 2'])
    input5 = st.selectbox('sub Category',sub_cat)
    input6 = st.number_input('Quantity',1,200)
    input7 = st.selectbox('Procurement Process',['Competetive Bid','Non-Competetive Bid'])
    input8 = st.date_input('Tender Invitation Date')
    input9 = st.date_input('Deadline for Submissions')
    input10 = st.number_input('Number of Bids Received')
    input11 = st.number_input('Buying Price')
    input12 = st.date_input('Purchase Date')
    input13 = st.number_input('Total Buying Price')

    if st.button('Predict'):
        days_to_submit,diff = days_xtract(input8,input9,input12)
        #to_predict_list = [input1,input2,input3,input4,input5,input6,input7,input10,input11,input13,days_to_submit,diff]
        #result = value_predictor(to_predict_list)
        st.success('Output is {},{}'.format(days_to_submit,diff))

if __name__=='__main__':
    main()