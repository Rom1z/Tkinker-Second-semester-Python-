from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Киска")
        self.setGeometry(300,250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()
    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction("Открыть", self.action_cliked)
        fileMenu.addAction("Сохранить", self.action_cliked)
    @QtCore.pyqtSlot()
    def action_cliked(self):
        action = self.sender()
        if action.text() == "Открыть":
            fname = QFileDialog.getOpenFileName(self)[0]

            try:
                f = open(fname, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
                print("No No No")

            f.close()


        elif action.text() == "Сохранить":
            fname = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(fname, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("No No No")




def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
