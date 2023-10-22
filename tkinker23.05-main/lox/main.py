import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class Win(QMainWindow):
    def __init__(self):
        super(Win,self).__init__()


def add_label():
    print("add")
def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400,400,300)
    win.setWindowTitle("Простая программа")

    btn = QtWidgets.QPushButton(win)
    btn.move(70,150)
    btn.setText("Нажми на меня")
    btn.setFixedWidth(200)
    btn.clicked.connect(add_label)


#Label Text
    label= QLabel(win)
    label.setText("Это программа ")
    label.move(100,100)

    win.show()
    sys.exit(app.exec_())

main()