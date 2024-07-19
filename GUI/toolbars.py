from PyQt6.QtWidgets import (
    QMainWindow,
    QToolBar
)


class toolbars(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

    def createToolBar(self):
        try:
            tools = QToolBar()
            tools.addAction("Exit", self.close)
            self.addToolBar(tools)
        except Exception as ex:
            print(ex.args)