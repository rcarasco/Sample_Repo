import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = QLabel("Work! Work! Work!")

        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    

app = QApplication(sys.argv)

window = MainWindow()
window.setGeometry(700,200,500,300)
window.show() 

app.exec_()
#commnent comment
