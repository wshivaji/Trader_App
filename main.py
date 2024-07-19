from GUI.main_window import Window
import sys

from PyQt6.QtWidgets import (
    QApplication
)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
