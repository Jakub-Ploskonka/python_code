from setuptools import setup

APP = ['gui.py']  # nazwa twojego pliku głównego
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt6'],
    'iconfile': 'app.icns',  # opcjonalnie: ikona w formacie .icns
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
