import sys

import streamlit as st
from streamlit.web import cli as stcli

from lib import my_lib


def main():
    my_lib.remove_deploy_button(st)
    st.success('Your streamlit app is running!')
    st.balloons()


if __name__ == '__main__':
    if st.runtime.exists():
        main()
    else:
        sys.argv = [
            "streamlit",
            "run",
            sys.argv[0],
            # add your own Streamlit command-line options here
            "--global.developmentMode=false",
        ]
        sys.exit(stcli.main())
