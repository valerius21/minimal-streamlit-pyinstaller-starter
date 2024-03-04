import time
import sys

import streamlit as st
from streamlit.web import cli as stcli


def main():
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success('Done!')
    st.balloons()


if __name__ == '__main__':
    if st.runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
