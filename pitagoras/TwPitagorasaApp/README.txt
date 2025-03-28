Instrukcja:

1. Utwórz środowisko:
   python3.10 -m venv .venv
   source .venv/bin/activate

2. Zainstaluj zależności:
   pip install --upgrade pip setuptools wheel
   pip install py2app PyQt6

3. Zbuduj aplikację:
   python3 setup.py py2app

4. Znajdziesz plik gui.app w folderze dist/