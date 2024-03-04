import streamlit as st

from lib import my_lib


def run_app():
    my_lib.remove_deploy_button(st)
    st.success('Your streamlit app is running!')
    st.balloons()


run_app()
