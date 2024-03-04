# Minimal Streamlit PyInstaller Starter

A minimal starter for effortlessly transforming your Streamlit apps into standalone desktop applications using
PyInstaller.

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Setup

1. **Clone the Repository**

```bash
git clone https://github.com/valerius21/minimal-streamlit-pyinstaller-starter.git
cd minimal-streamlit-pyinstaller-starter
```

2. **Create a Virtual Environment**

```bash
python -m venv .venv
```

Activate the virtual environment:

- On Windows: `.venv\Scripts\activate`
- On Unix or MacOS: `source .venv/bin/activate`

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Prepare the Application Spec File**

Copy the `streamlit_app.spec.example` to `streamlit_app.spec`:

```bash
cp streamlit_app.spec.example streamlit_app.spec
```

Modify `streamlit_app.spec` as needed to fit your application's requirements.

### Running Your Streamlit App

```bash
streamlit run streamlit_app.py
```

### Building Your Standalone Application

```bash
./2_build.sh
```

After building, your standalone application can be found in the `dist` directory. You can move it anywhere.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

