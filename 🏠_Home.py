from streamlit import session_state as state
import streamlit as st
from PIL import Image
from pathlib import Path
import logging

st.set_page_config(
    page_title="Home | C-MIND 1.0 App",
    page_icon="🏠",
)

PATH = '.'
# PATH = Path(Path(__file__).resolve()).parent
# logger = logging.getLogger(__name__)

state['login'] = False
state['PATH'] = PATH

st.markdown('<h3 style=\'text-align:center;\'>Welcome to C-MIND 1.0! 👋</h3>', unsafe_allow_html=True)

image1 = Image.open(f'{PATH}/data/images/cover_1.png')
image2 = Image.open(f'{PATH}/data/images/cover_2.png')

st.image(image1)
st.image(image2)