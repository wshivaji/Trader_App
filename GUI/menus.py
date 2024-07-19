from PyQt6.QtWidgets import (
    QMainWindow
)


class menus(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

    def createMenu(self):
        try:
            menu = self.menuBar().addMenu("&Menu")
            menu.addAction("&Exit", self.close)
        except Exception as ex:
            print(ex.args)
