import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from TwPitagorasa import TwPitagorasa


class OknoPitagoras(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Twierdzenie Pitagorasa")
        self.kalkulator = TwPitagorasa()
        self.init_ui()

    def init_ui(self):
        # Pola wejściowe
        self.label_a = QLabel("Podaj a:")
        self.entry_a = QLineEdit()

        self.label_b = QLabel("Podaj b:")
        self.entry_b = QLineEdit()

        # Przycisk "Oblicz"
        self.btn_oblicz = QPushButton("Oblicz c")
        self.btn_oblicz.clicked.connect(self.oblicz)

        # Przycisk "Reset"
        self.btn_reset = QPushButton("Reset")
        self.btn_reset.clicked.connect(self.resetuj)

        # Etykieta na wynik
        self.label_wynik = QLabel("Przeciwprostokątna c =")

        # Layouty
        layout = QVBoxLayout()

        # Wiersz 1
        wiersz1 = QHBoxLayout()
        wiersz1.addWidget(self.label_a)
        wiersz1.addWidget(self.entry_a)

        # Wiersz 2
        wiersz2 = QHBoxLayout()
        wiersz2.addWidget(self.label_b)
        wiersz2.addWidget(self.entry_b)

        # Wiersz 3 – przyciski
        wiersz3 = QHBoxLayout()
        wiersz3.addWidget(self.btn_oblicz)
        wiersz3.addWidget(self.btn_reset)

        layout.addLayout(wiersz1)
        layout.addLayout(wiersz2)
        layout.addLayout(wiersz3)
        layout.addWidget(self.label_wynik)

        self.setLayout(layout)

    def oblicz(self):
        try:
            a = float(self.entry_a.text())
            b = float(self.entry_b.text())
            wynik = self.kalkulator.oblicz_c(a, b)
            self.label_wynik.setText(f"Przeciwprostokątna c = {wynik}")
        except ValueError:
            QMessageBox.critical(self, "Błąd", "Podaj poprawne liczby.")

    def resetuj(self):
        self.entry_a.clear()
        self.entry_b.clear()
        self.label_wynik.setText("Przeciwprostokątna c =")
        self.entry_a.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = OknoPitagoras()
    okno.show()
    sys.exit(app.exec())
