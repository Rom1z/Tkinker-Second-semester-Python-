import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

def click():
    print("Hy Button is clicked!")

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400,400,300)
    win.setWindowTitle("Pyqt5 Tutorial")

#Button Click
    button = QtWidgets.QPushButton(win)
    button.setText("Hi! Click Me")
    button.move(100,100)
    button.clicked.connect(click)

    win.show()
    sys.exit(app.exec_())

main()
