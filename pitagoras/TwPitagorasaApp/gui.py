from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from TwPitagorasa import TwPitagorasa
import sys

class Okno(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Twierdzenie Pitagorasa")
        self.kalkulator = TwPitagorasa()

        self.label_a = QLabel("Podaj a:")
        self.input_a = QLineEdit()
        self.label_b = QLabel("Podaj b:")
        self.input_b = QLineEdit()

        self.button_oblicz = QPushButton("Oblicz c")
        self.button_oblicz.clicked.connect(self.oblicz)

        self.label_wynik = QLabel("Przeciwprostokątna c = ")

        layout = QVBoxLayout()
        layout.addWidget(self.label_a)
        layout.addWidget(self.input_a)
        layout.addWidget(self.label_b)
        layout.addWidget(self.input_b)
        layout.addWidget(self.button_oblicz)
        layout.addWidget(self.label_wynik)

        self.setLayout(layout)

    def oblicz(self):
        try:
            a = float(self.input_a.text())
            b = float(self.input_b.text())
            wynik = self.kalkulator.oblicz_c(a, b)
            self.label_wynik.setText(f"Przeciwprostokątna c = {wynik}")
        except ValueError:
            QMessageBox.critical(self, "Błąd", "Podaj poprawne liczby.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())