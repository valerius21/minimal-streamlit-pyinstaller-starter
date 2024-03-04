"""This example module contains helper functions for your app."""
import streamlit


def remove_deploy_button(st: streamlit):
    """Remove the deploy-button from the Streamlit app."""
    st.markdown("""
        <style>
            .reportview-container {
                margin-top: -2em;
            }
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            #stDecoration {display:none;}
        </style>
    """, unsafe_allow_html=True)
