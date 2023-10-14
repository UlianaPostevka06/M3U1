from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow
from passwword import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication([])
ex = Widget

def generation():
    digital = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter = ['f', 'r', 'a', 'd']
bt_ok.clicked.connect(generation)

ex.show()
app.exec_() 
