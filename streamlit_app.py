import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(
  page_title ='Niks portofolio',
  page_icon = '🚀',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.set_page_config('''
                        <style>  
                            .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                            .sub-header {font_size: 24px; text-align:center; color: #666;}
                        </style>
                     ''',unsafe_allow_html = True)


#Sidebar
st.sidebar.title('📍Navigation')
page = st.sidebar.radio('Go to',
                        ['🏡 Home', '🚶🏾‍♂️ About', '📁 Projects', '🔧 Skills', '📝 Resume', '📩 Contact'])
                        
                 
