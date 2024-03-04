#!/bin/sh
pyinstaller --onefile --additional-hooks-dir=./hooks streamlit_app.py --clean
