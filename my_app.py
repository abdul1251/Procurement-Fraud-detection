import streamlit as st
from joblib import load
import numpy as np
from datetime import datetime

def lable_encode(input1,input2,input3,input4,input5,input7):
    ap_of = app_officer.index(input1)
    re_of = req_officer.index(input2)
    sup = supplier.index(input3)
    cat = category.index(input4)
    sub = sub_cat.index(input5)
    Pro_pro = procure_process.index(input7)
    return ap_of,re_of,sup,cat,sub,Pro_pro


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
	loaded_model = load("filename.joblib")
	result = loaded_model.predict(to_predict)
	return result[0]

html_temp = """
<div style = "background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Procurement Fraud detection </h2>
</div>"""

def main():
    global app_officer
    app_officer = ['Rowney Cortin', 'Karol Ferre', 'Adelbert Heindrich', 'Wilone Kaufman', 'Jasper Raccio', 'Krista Helin', 'Leoline Emlin', "Laure O'Sharry", 'Parry Shiel', 'Rafael Penchen', 'Jolene Hamby', 'Eleanora Pattlel', 'Morry MacGibbon', 'Sauveur Da Costa', "Donni O'Shiel", 'Matthiew Tolley', 'Genny Doherty', 'Amos Brusby', 'Shanda Chaston', 'Clarita Alldred', 'Malissa Wenderoth', 'Shandra McChruiter', 'Brigit Pickle', 'Jemima Girdler', 'Sophronia Gennrich', 'Tabbi Rounsefull', 'Misha Brendel', 'Doralyn Jimeno', 'Lucian Tettley', 'Analise Gamon', 'Pandora Couper', 'Pavlov McNirlan', 'Shaine Bate', 'Parry Puig', 'Chadwick Demelt', 'Thatch Basterfield', 'Tonnie Kesteven', 'Mattie Speeding', 'Bowie Magenny', 'Lyn Arenson', 'Kerry Plet', 'Ethelyn Charrington', 'Lenora Titmuss', 'Etan Messent', 'Stormie Deery']
    global req_officer
    req_officer = ['Bunny Spraggs', "Lorrayne O' Lone", 'Nicolette Convery', 'Reuben Chiommienti', 'Ely Gwinnel', 'Ofilia Borrington', 'Batsheva Danslow', 'Lesly Hallifax', 'Rebekah Jermy', 'Silvie Whittock', 'Jocelin Figg', 'Tris Lerer', 'Torey Falconer-Taylor', 'Kiah Friday', 'Bradney Legon', 'Carline Ezzy', 'Marget Metts', 'Yorke Schuricke', 'Tootsie Ganing', 'Lars Laraway', 'Dorothee Cahey', 'Marshall Fanshawe', 'Torry Vamplus', 'Sofia Plumbe', 'Joey Gallehock', 'Benita Maker', 'Perry Pieter', 'Hannah Shildrick', 'Beryle Menicomb', 'Lloyd Cavaney', 'Llewellyn Iacovacci', 'Anthiathia Treen', 'Susannah Sangar', 'Jayme Birth', 'Gloriana Vaz']
    global supplier
    supplier = ['Rosenbaum Group', 'Botsford, Rolfson and Pouros', 'Ferry-Dibbert', 'Gusikowski Group', 'Hartmann Inc', 'Friesen-Ullrich', 'Ward-Wolff', 'Swift-Friesen', 'Cummerata, Gibson and Herman', 'Howell, Haley and Cremin', 'Bogan-Gerhold', 'Rosenbaum-Jones', 'Kirlin, Kutch and Tremblay', 'Hessel-Bergnaum', 'Ruecker, Senger and Feeney', 'Pouros-Mitchell', 'Witting Group', 'Tillman-Larson', 'Monahan-Rippin', 'Miller-Lueilwitz', 'Denesik LLC', 'Ryan, Turner and Schulist', 'Rohan-Runolfsdottir', 'Hagenes, Kilback and Conroy', 'Koepp, Zulauf and Bins', 'Krajcik, Fritsch and Ebert', 'Smith, Cummings and Auer', 'Wuckert-Effertz', 'Schmitt-Kling', 'Rutherford, Murphy and Jast', 'Rogahn and Sons', 'Jacobs, Senger and Dickens', 'Ratke-Morissette', 'Sipes Inc', 'Bartell, Swaniawski and Kuhlman', 'Kuvalis-Schiller', 'Spinka-Price', 'Hills-Rau', 'Hammes Inc', 'Ward, Wisoky and Kiehn', 'Bartell, Lemke and MacGyver', 'Shanahan, Watsica and Mayert', 'Schuster, Huels and Rolfson', 'Herman and Sons', 'Paucek and Sons', 'Sanford LLC', 'Koelpin-Brown', 'Nolan, Bahringer and Torphy', 'Leffler Inc', 'Bayer, Haley and Hermann', 'Lebsack, Herzog and Mraz', "Maggio, O'Kon and McClure", 'Sipes-Schroeder', 'Bauch Inc', 'Wilkinson Inc', 'Klein, Kilback and Wisozk', 'Dare, Barrows and Gottlieb', 'Metz LLC', 'Waters and Sons', 'Lind Group', 'Reynolds, Dooley and Doyle', 'Walsh Group', 'Franecki-Kulas', 'Ward, Larkin and Swift', 'Graham, Little and Kris', 'Vandervort, Nader and Reichert', 'Thompson-Lowe', 'Cassin-Langosh', 'Murazik, Conn and Rodriguez', 'Cummings-Gleason', 'Denesik Group', 'Marvin, Legros and Hoppe', 'Gutkowski-Lynch', 'Toy-Ferry', 'Wehner-Stehr', 'Schiller-Cremin', 'Kunze, Von and Leannon', 'Mante Inc', 'Lockman-Torphy', 'Legros-Jacobs', 'Stanton-West', 'Maggio, Hahn and Jones', 'Wolff, Wisozk and Fisher', 'Yundt, Johns and Cole', 'Hintz Inc', 'Boyle, Price and Jacobson', 'Prosacco LLC', 'Hamill, Walsh and Volkman', 'Stamm LLC', 'Prohaska-Shanahan', 'Funk, Marks and Zboncak', 'Greenholt and Sons', 'Blick-Farrell', 'Stanton, Haley and Ruecker', 'Harber, Runte and Glover', 'Kohler-Zieme', 'Ernser, Nolan and Marquardt', 'Kreiger and Sons']
    global category
    category = ['Beverages', 'Seafood', 'Dairy', 'Cleaning_products', 'Canned_foods', 'Frozen']
    global sub_cat
    sub_cat = ['Juice','Crab','Yogurt','Sponges / Scrubbers','Broth','Burritos','Milk','Lobster','Butter / Margarine','Salmon','Applesauce','Cottage cheese','Air freshener','Vegetables','Catfish','Beer','Bleach / Detergent','Olives','Soda/Pop','Baked beans','Veggies','Shrimp','Wine','Garbage bags','Glass cleaner','Vacuum bags','Pizza','Breakfasts','Sports Drinks']
    global procure_process
    procure_process = ['Competetive Bid','Non-Competetive Bid']

    st.title("Procurement Fraud Detection")
    st.markdown(html_temp,unsafe_allow_html=True)
    input1 = st.selectbox('Approving Officer Name',app_officer)
    input2 = st.selectbox('Requesting Officer Name',req_officer)
    input3 = st.selectbox('Supplier Name',supplier)
    input4 = st.selectbox('Product Category',category)
    input5 = st.selectbox('sub Category',sub_cat)
    input6 = st.number_input('Quantity',1,200)
    input7 = st.selectbox('Procurement Process',procure_process)
    input8 = st.date_input('Tender Invitation Date')
    input9 = st.date_input('Deadline for Submissions')
    input10 = st.number_input('Number of Bids Received')
    input14 = st.number_input('Unit_price',1,1000)
    input11 = st.number_input('Buying Price',1,1000)
    input12 = st.date_input('Purchase Date')
    input13 = st.number_input('Total Buying Price',1,10000)


    if st.button('Predict'):
        ap_of,re_of,sup,cat,sub,Pro_pro = lable_encode(input1,input2,input3,input4,input5,input7)
        days_to_submit,diff = days_xtract(input8,input9,input12)
        to_predict_list = [ap_of,re_of,sup,cat,sub,input6,Pro_pro,input10,input14,input11,input13,days_to_submit,diff]
        result = value_predictor(to_predict_list)
        st.success('Output is {}'.format(result))

if __name__=='__main__':
    main()
