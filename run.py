import streamlit_app

import streamlit.web.cli as stcli
import os
import sys


def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("streamlit_app.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
