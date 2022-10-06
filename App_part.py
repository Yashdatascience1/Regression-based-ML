import streamlit as st
import streamlit.components.v1 as stc
import EDA_part
import ML_part

from EDA_part import run_Cap_EDA
from ML_part import run_Cap_ML


html_temp = """
		<div style="background-color:#FA8072;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Determining the CTC to be offered to a new candidate </h1>
		</div>"""
def main():
    stc.html(html_temp)
    menu = ["Home","EDA","ML"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.markdown("""
                    ### Title: CTC prediction app
                    #### Dataset source
                    This dataset contains educational and professional information about the candidate applying

                        - https://drive.google.com/file/d/1N_9Bg6o_3A_bmvsx6fh6ohJnrmWUNOI4/view
 
                    #### App contents
                    - EDA -  Exploratory analysis of Data
                    - ML - Predict the CTC to be offered to a new candidate

                        """)
    elif choice == "EDA":
        run_Cap_EDA()
    elif choice == "ML":
        run_Cap_ML()
    
if __name__ == '__main__':
    main()