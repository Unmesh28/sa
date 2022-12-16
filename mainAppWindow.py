import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal,QObject
from mainWindow import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.worker = Worker()
        self.worker.sig.connect(self.updatelabel)
        self.x=0
        self.setupUi(self)

    def keyPressEvent(self, event):
        global img_no

        if self.toggle_State == 0:
            img_no = 28
        elif self.toggle_State == 1:
            img_no = 8

        if event.key() == Qt.Key_1:
            self.changeImg(1, img_no)
        if event.key() == Qt.Key_2:
            self.changeImg(2, img_no)
        if event.key() == Qt.Key_3:
            self.changeImg(3,img_no)
        if event.key() == Qt.Key_4:
            self.changeImg(4, img_no)
        if event.key() == Qt.Key_5:
            self.changeImg(5, img_no)
        if event.key() == Qt.Key_6:
            self.changeImg(6, img_no)
        if event.key() == Qt.Key_7:
            self.changeImg(7, img_no)
        if event.key() == Qt.Key_8:
            self.changeImg(8, img_no)
        if event.key() == Qt.Key_A:
            for i in range(1, 9):
                if self.toggle_State == 0:
                    self.changeImg(i, i)
                elif self.toggle_State == 1:
                    self.changeImg(i, 20+i)




if __name__ == '__main__':
    app = QApplication([])
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())