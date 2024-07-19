import sys
from GUI.menus import menus
from GUI.toolbars import toolbars
from GUI.status_bar import status_bar
from PyQt6.QtCore import Qt
# from menus import menus
# from toolbars import toolbars
# from status_bar import status_bar
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QGridLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)


class Window(QMainWindow):
    def __init__(self):
        self.WINDOW_SIZE = 500
        self.DISPLAY_HEIGHT = 200
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self.setFixedSize(self.WINDOW_SIZE, self.WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        Window._createDisplay(self)

        menus.createMenu(self)
        toolbars.createToolBar(self)
        status_bar.createStatusBar(self)


    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(self.DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
