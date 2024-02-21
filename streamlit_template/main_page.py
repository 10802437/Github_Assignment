import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see racer or kart stats")

link = '[Link to my GitHub Pages Site]https://10802437.github.io/Github_Assignment/'
st.markdown(link, unsafe_allow_html=True)