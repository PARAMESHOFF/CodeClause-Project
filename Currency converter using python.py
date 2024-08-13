import streamlit as st
import requests
st.markdown('<iframe src="https://lottie.host/embed/fd41f21d-74b3-4438-83fa-19dab9b4d9fe/7ICXOXSBwL.json"> width=100%</iframe>',unsafe_allow_html=True)



col1,col3=st.columns(2)
with col1:
    base_currency=st.selectbox('currency1',['USD','INR','EUR','CHF','SGD'])


with col3:
    target_currency=st.selectbox('currency2',['USD','INR','EUR','CHF','SGD'])


amount = st.number_input("Enter the amount to convert", min_value=0.0, format="%.2f")

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

if st.button("Convert"):
    if base_currency != target_currency:
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        converted_amount = amount * exchange_rate
        col1,col2=st.columns(2)
        with col1:
            st.write(f"{amount} {base_currency}")
        with col2:  
            st.write(f"{converted_amount:.2f} {target_currency}")

    else:
        st.write("Base currency and target currency cannot be the same.")


st.markdown('<style> body{text-align:center;} #MainMenu, footer {visibility: hidden;) .stApp stAppEmbeddingId-sh8g35c4zjul st-emotion-cache-1r4qj8v erw9t6i1{background-color:bule;} </style>',
unsafe_allow_html=True)