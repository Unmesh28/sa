import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QObject
#from mydialog import Ui_mydialog

class Communicate(QObject):
    sig = pyqtSignal(str) 

class Mainwindow(QtWidgets.QMainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(Mainwindow, self).__init__(*args, **kwargs)
        #self.setupUi(self)
        self.communicate = Communicate()
        self.communicate.sig[str].connect(self.updatelabel)

        self.thread = Worker(communicate = self.communicate)
        #self.loop = loop() # this seems useless to me here
        
        self.mypushbutton.clicked.connect(self.mypushbuttonclicked)


    def mypushbuttonclicked(self):
        self.thread.start()

    def updatelabel(self, text):
        self.mylabel.setText(text)

class Worker(QThread):

    def __init__(self, parent=None, communicate=Communicate()):
        super(Worker, self).__init__(parent)
        self.communicate = communicate
        # self.count = 0
        self.loop = loop(communicate= self.communicate)

    def run(self):

        self.loop.methodA()

        ## Original code without being in class loop and method loopA
        # while True:
        #     time.sleep(1)
        #     self.count += 1
        #     if (self.count % 1 == 0):
        #         self.sig.emit(f"Timer: {self.count} s")

# Newly added class with method "methodA"
class loop(object):

    def __init__(self, communicate=Communicate()):
        self.count = 0
        self.communicate = communicate

    def methodA(self):

        while True:
            time.sleep(1)
            self.count += 1
            if (self.count % 1 == 0):
                self.communicate.sig.emit(f"Timer: {self.count} s")



app = QtWidgets.QApplication(sys.argv)
window = Mainwindow()
app.setStyle("Fusion")
window.show()
app.exec()