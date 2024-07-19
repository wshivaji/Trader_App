from PyQt6.QtWidgets import (
    QMainWindow,
    QStatusBar
)


class status_bar(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

    def createStatusBar(self):
        try:

            status = QStatusBar()
            status.showMessage("I'm the Status Bar")
            self.setStatusBar(status)
        except Exception as ex:
            print(ex.args)
