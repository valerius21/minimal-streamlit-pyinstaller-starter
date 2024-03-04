#!/bin/sh
# Generate spec file, then modify it
pyinstaller --onefile --additional-hooks-dir=./hooks streamlit_app.py --clean
