
from functools import partial
import pyautogui
from PyQt5 import QtCore, QtWidgets
from datetime import datetime

from PyQt5.QtCore import QPoint, QEasingCurve, QPropertyAnimation
from PyQt5.QtWidgets import QButtonGroup
from Thread import WorkerThread



from secondWindow import Ui_secondWindow


class Ui_MainWindow(object):

    btn_state = [0,0,0,0,0,0,0,0]
    toggle_State = 0

    def setupUi(self, MainWindow):



        global bat_start, bat_len, Starting_point, btn_height, btn_width, bottom_btn_height, top_btn_height, Starting_point_y, Starting_point_x, margin, back_fac, btn_text,buttonPadcolor,padding ,width_rows,width
        MainWindow.setObjectName("MainWindow")

        width, height = pyautogui.size()

        # width = 1437
        # height =900

        if width >= 1800:
            btn_width =int(width/16)
            margin = int(height / 20)
            back_fac=1
        elif width < 1800:
            btn_width =int(width/5)
            margin = int(height / 38)
            back_fac=0.5

        Starting_point = int((width / 20) * 1)
        top_btn_height = int(height / 12)
        Starting_point_y = int((width / 10) * 1.2)
        bottom_btn_height = int(top_btn_height * 4.5)
        Starting_point_x = int((width / 10) * 1)
        width_rows = int((width / 10) * 8)
        btn_text = int(bottom_btn_height/16)

        padding = int(height/30)

        buttonPadcolor = "#FFFFFF"

        MainWindow.resize(width, height)
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")





        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, width,height))
        self.background.setStyleSheet("image: url(images/Background.png);")
        self.background.setText("")
        self.background.setScaledContents(True)
        self.background.setObjectName("Background")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(int(margin+Starting_point_x), Starting_point_y, int(width_rows-2*margin), top_btn_height))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.firstRow = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.firstRow.setContentsMargins(0, 0, 0, 0)
        self.firstRow.setObjectName("firstRow")

        self.backFirstRow = QtWidgets.QLabel(self.centralwidget)
        self.backFirstRow.setGeometry(QtCore.QRect(int(Starting_point_x+margin), int(Starting_point_y-top_btn_height/4), int(width_rows-margin*2), int(top_btn_height*(3/2))))
        self.backFirstRow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:15px;")
        self.backFirstRow.setText("")
        self.backFirstRow.setObjectName("backFirstRow")




        self.btn1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn1.setStyleSheet("#btn1{\n"
                                "background:none;\n"
                                "border: none;\n"
                                "background-repeat: none;\n"
                                "height:" + str(top_btn_height) + "px;\n"
                                                                  "image: url(images/thumb_1.png);\n"
                                                                  "}\n"
                                                                  "")
        self.btn1.setText("")
        self.btn1.setObjectName("btn1")
        self.firstRow.addWidget(self.btn1)

        self.btn1.clicked.connect(partial(self.clicked_btn, 1))

        self.btn2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn2.setStyleSheet("#btn2{\n"
                                "background:none;\n"
                                "border: none;\n"
                                "background-repeat: none;\n"
                                "height:" + str(top_btn_height) + "px;\n"
                                                                  "image: url(images/thumb_2.png);\n"
                                                                  "}\n"
                                                                  "")
        self.btn2.setText("")
        self.btn2.setObjectName("btn2")
        self.firstRow.addWidget(self.btn2)
        self.btn2.clicked.connect(partial(self.clicked_btn, 2))

        self.btn3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn3.setStyleSheet("#btn3{\n"
                                "background:none;\n"
                                "border: none;\n"
                                "background-repeat: none;\n"
                                "height:" + str(top_btn_height) + "px;\n"
                                                                  "image: url(images/thumb_3.png);\n"
                                                                  "}\n"
                                                                  "")
        self.btn3.setText("")
        self.btn3.setObjectName("btn3")
        self.firstRow.addWidget(self.btn3)
        self.btn3.clicked.connect(partial(self.clicked_btn, 3))

        self.btn4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn4.setStyleSheet("#btn4{\n"
                                "background:none;\n"
                                "border: none;\n"
                                "background-repeat: none;\n"
                                "height:" + str(top_btn_height) + "px;\n"
                                                                  "image: url(images/thumb_4.png);\n"
                                                                  "}\n"
                                                                  "")
        self.btn4.setText("")
        self.btn4.setObjectName("btn4")
        self.firstRow.addWidget(self.btn4)
        self.btn4.clicked.connect(partial(self.clicked_btn, 4))

        self.btn5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn5.setStyleSheet("#btn5{\n"
                                "background:none;\n"
                                "border: none;\n"
                                "background-repeat: none;\n"
                                "height:" + str(top_btn_height) + "px;\n"
                                                                  "image: url(images/thumb_5.png);\n"
                                                                  "}\n"
                                                                  "")
        self.btn5.setText("")
        self.btn5.setObjectName("btn5")
        self.firstRow.addWidget(self.btn5)
        self.btn5.clicked.connect(partial(self.clicked_btn, 5))


        # self.btn6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        # self.btn6.setStyleSheet("#btn6{\n"
        #                         "background:none;\n"
        #                         "border: none;\n"
        #                         "background-repeat: none;\n"
        #                         "height:" + str(top_btn_height) + "px;\n"
        #                                                           "image: url(images/thumb_6.png);\n"
        #                                                           "}\n"
        #                                                           "")
        # self.btn6.setText("")
        # self.btn6.setObjectName("btn6")
        # self.firstRow.addWidget(self.btn6)
        # self.btn6.clicked.connect(partial(self.clicked_btn, 6))
        #
        # self.btn7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        # self.btn7.setStyleSheet("#btn7{\n"
        #                         "background:none;\n"
        #                         "border: none;\n"
        #                         "background-repeat: none;\n"
        #                         "height:" + str(top_btn_height) + "px;\n"
        #                                                           "image: url(images/thumb_7.png);\n"
        #                                                           "}\n"
        #                                                           "")
        # self.btn7.setText("")
        # self.btn7.setObjectName("btn7")
        # self.firstRow.addWidget(self.btn7)
        # self.btn7.clicked.connect(partial(self.clicked_btn, 7))
        #
        # self.btn8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        # self.btn8.setStyleSheet("#btn8{\n"
        #                         "background:none;\n"
        #                         "border: none;\n"
        #                         "background-repeat: none;\n"
        #                         "height:" + str(top_btn_height) + "px;\n"
        #                                                           "image: url(images/thumb_8.png);\n"
        #                                                           "}\n"
        #                                                           "")
        # self.btn8.setText("")
        # self.btn8.setObjectName("btn8")
        # self.firstRow.addWidget(self.btn8)
        # self.btn8.clicked.connect(partial(self.clicked_btn, 8))



        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(Starting_point_x, int(Starting_point_y+2*top_btn_height), width_rows, int(bottom_btn_height)))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.secondRow = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.secondRow.setContentsMargins(0, 0, 0, 0)
        self.secondRow.setObjectName("secondRow")

        self.btn9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn9.setStyleSheet("#btn9{\n"
                                 "background:none;\n"
                                 "border: 1px solid #3FA796;\n"
                                 "background-repeat: none;\n"
                                 "height:" + str(bottom_btn_height) + "px;\n"
                                                                      "width:" + str(btn_width) + "px;\n"
                                                                      "text-align: bottom;\n"
                                                                      "font-size: " + str(btn_text) + "px;\n"
                                                                      "image: url(images/thumb_9.png);\n"
                                                                      "font-weight: bold;\n"
                                                                      "padding-bottom: " + str(padding) + "px;\n"
                                                                      "padding-top: 0px;\n" 
                                                                      "background-color:" + buttonPadcolor + ";\n"
                                                                      "border-radius:30px;\n"
                                                                      "margin: " + str(margin) + "px;\n"
                                                                      "margin-bottom: 0px;\n"
                                                                      "font-family: Arial, Helvetica, sans-serif;\n"
                                                                      "color:Black;}")
        self.btn9.setObjectName("btn9")
        self.secondRow.addWidget(self.btn9)
        self.btn9.clicked.connect(partial(self.clicked_btn, 9))


        self.btn10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn10.setStyleSheet("#btn10{\n"
                                 "background:none;\n"
                                 "border: 1px solid #3FA796;\n"
                                 "background-repeat: none;\n"
                                 "height:" + str(bottom_btn_height) + "px;\n"
                                                                      "width:" + str(btn_width) + "px;\n"
                                                                      "text-align: bottom;\n"
                                                                      "font-size: " + str(btn_text) + "px;\n"
                                                                      "image: url(images/thumb_10.png);\n"
                                                                      "font-weight: bold;\n"
                                                                      "padding-bottom: " + str(padding) + "px;\n"
                                                                      "padding-top: 0px;\n" 
                                                                      "background-color:" + buttonPadcolor + ";\n"
                                                                      "border-radius:30px;\n"
                                                                      "margin: " + str(margin) + "px;\n"
                                                                      "margin-bottom: 0px;\n"
                                                                      "font-family: Arial, Helvetica, sans-serif;\n"
                                                                      "color:Black;}")
        self.btn10.setObjectName("btn10")
        self.secondRow.addWidget(self.btn10)
        self.btn10.clicked.connect(partial(self.clicked_btn, 10))



        self.btn11 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn11.setStyleSheet("#btn11{\n"
                                 "background:none;\n"
                                 "border: 1px solid #3FA796;\n"
                                 "background-repeat: none;\n"
                                 "height:" + str(bottom_btn_height) + "px;\n"
                                                                      "width:" + str(btn_width) + "px;\n"
                                                                      "text-align: bottom;\n"
                                                                      "font-size: " + str(btn_text) + "px;\n"
                                                                      "image: url(images/thumb_11.png);\n"
                                                                      "font-weight: bold;\n"
                                                                      "padding-bottom: " + str(padding) + "px;\n"
                                                                      "padding-top: 0px;\n" 
                                                                      "background-color:" + buttonPadcolor + ";\n"
                                                                      "border-radius:30px;\n"
                                                                      "margin: " + str(margin) + "px;\n"
                                                                      "margin-bottom: 0px;\n"
                                                                      "font-family: Arial, Helvetica, sans-serif;\n"
                                                                      "color:Black;}")
        self.btn11.setObjectName("btn11")
        self.secondRow.addWidget(self.btn11)
        self.btn11.clicked.connect(partial(self.clicked_btn, 11))


        self.btn12 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn12.setStyleSheet("#btn12{\n"
                                 "background:none;\n"
                                 "border: 1px solid #3FA796;\n"
                                 "background-repeat: none;\n"
                                 "height:" + str(bottom_btn_height) + "px;\n"
                                                                      "width:" + str(btn_width) + "px;\n"
                                                                      "text-align: bottom;\n"
                                                                      "font-size: " + str(btn_text) + "px;\n"
                                                                      "image: url(images/thumb_12.png);\n"
                                                                      "font-weight: bold;\n"
                                                                      "padding-bottom: " + str(padding) + "px;\n"
                                                                      "padding-top: 0px;\n" 
                                                                      "background-color:" + buttonPadcolor + ";\n"
                                                                      "border-radius:30px;\n"
                                                                      "margin: " + str(margin) + "px;\n"
                                                                      "margin-bottom: 0px;\n"
                                                                      "font-family: Arial, Helvetica, sans-serif;\n"
                                                                      "color:Black;}")
        self.btn12.setObjectName("btn12")
        self.secondRow.addWidget(self.btn12)
        self.btn12.clicked.connect(partial(self.clicked_btn, 12))

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(Starting_point_x, int(Starting_point_y + 2 * top_btn_height), width_rows,int(bottom_btn_height)))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.BtnRow = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.BtnRow.setContentsMargins(0, 0, 0, 0)
        self.BtnRow.setObjectName("horizontalLayout_3")


        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.BtnRow.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.BtnRow.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.BtnRow.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.BtnRow.addWidget(self.label_4)

        self.backFirstRow.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_2.raise_()


        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.btn1)
        self.btn_grp.addButton(self.btn2)
        self.btn_grp.addButton(self.btn3)
        self.btn_grp.addButton(self.btn4)
        self.btn_grp.addButton(self.btn5)
        # self.btn_grp.addButton(self.btn6)
        # self.btn_grp.addButton(self.btn7)
        # self.btn_grp.addButton(self.btn8)
        self.btn_grp.addButton(self.btn9)
        self.btn_grp.addButton(self.btn10)
        self.btn_grp.addButton(self.btn11)
        self.btn_grp.addButton(self.btn12)


        self.ThreadOpen()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(int((width/40)), int(((height / 12) - (height / 18)) / 2), int(width/10),
                         int(height / 30)))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.statusBarCols = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.statusBarCols.setContentsMargins(0, 0, 0, 0)
        self.statusBarCols.setObjectName("statusBarCols")


        self.wifi = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.WiFi_Connected(True)
        self.wifi.setText("")
        self.wifi.setScaledContents(True)
        self.wifi.setObjectName("wifi")
        self.statusBarCols.addWidget(self.wifi)

        self.Bluetooth = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.BlueT_Connected(False)
        self.Bluetooth.setText("")
        self.Bluetooth.setScaledContents(True)
        self.Bluetooth.setObjectName("Bluetooth")
        self.statusBarCols.addWidget(self.Bluetooth)

        self.timeDis = QtWidgets.QLabel(self.centralwidget)
        self.timeDis.setGeometry(QtCore.QRect(int((width/16)*14.7), int(((height / 12) - (height / 18)) / 2),int(width/16), int(height / 30)))
        self.timeDis.setStyleSheet("text-position:centre;\n"
                                   "padding-left:10px;\n"
                                    "border:none;\n"
                                    "font-size: 25px;\n"
                                    "font-weight: bold;\n"
                                    "font-family: Arial, Helvetica, sans-serif;\n"
                                    "color:#FFFFFF;")
        self.timeDis.setAlignment(QtCore.Qt.AlignCenter)
        self.timeDis.setObjectName("timeCol")
        nowtime = datetime.now()
        current_time = nowtime.strftime("%H:%M")
        self.update_Time(current_time)

        self.changeImg(0,0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.toggleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.toggleBtn.setGeometry(QtCore.QRect(int(width/2-50), int(Starting_point_y-100), 90, 42))
        self.toggleBtn.setText("")
        self.toggleBtn.setStyleSheet("width:100px;\n"
                                     "height:50px;\n"
                                     "border-radius:20px;\n"
                                     "background: #3CCF4E;\n"
                                     # "border: 2.5px solid grey;"
                                     "border: none;")
        self.toggleBtn.setObjectName("pushButton")
        self.toggleBtn.clicked.connect(self.toggleTheme)

        self.toglabel = QtWidgets.QLabel(self.centralwidget)
        self.toglabel.setGeometry(QtCore.QRect(int(width/2-45), int(Starting_point_y-94), 30, 30))
        self.toglabel.setText("")
        self.toglabel.setStyleSheet("hieght:50px;\n"
                                 "width:50px;\n"
                                 "background-color:white;\n"
                                 "border-radius:15px;")
        self.toglabel.setObjectName("label")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn12.setText(_translate("MainWindow", "INFOTAINMENT"))
        self.btn11.setText(_translate("MainWindow", "GPS"))
        self.btn10.setText(_translate("MainWindow", "CRITICAL VIDEO\nRECORDING"))
        self.btn9.setText(_translate("MainWindow", "ADAS"))

    def toggleTheme(self):
        self.toggleAnimation()
        if (self.toggle_State==0):
            self.background.setStyleSheet("image: url(images/Background_D.png);")
            self.backFirstRow.setStyleSheet("background-color: rgba(3, 39, 50,220);\n"
                                            "border-radius:15px;")
            for i in range (1,9):
                self.changeImg(i,20+i)
            self.btn9.setStyleSheet("#btn9{\n"
                                    "background:none;\n"
                                    "border: none;\n"
                                    "background-repeat: none;\n"
                                    "height:" + str(bottom_btn_height) + "px;\n"
                                    "width:" + str(btn_width) + "px;\n"
                                    "text-align: bottom;\n"
                                    "font-size: " + str(btn_text) + "px;\n"
                                    "image: url(images/thumb_209.png);\n"
                                    "font-weight: bold;\n"
                                    "padding-bottom: " + str(padding) + "px;\n"
                                    "padding-top: 0px;\n"
                                    "background-color: rgba(3, 39, 50,0.8);\n" 
                                    "border-radius:30px;\n"
                                    "margin: " + str(margin) + "px;\n"
                                    "margin-bottom: 0px;\n"
                                    "font-family: Arial, Helvetica, sans-serif;\n"
                                    "color:White;}")
            self.btn10.setStyleSheet("#btn10{\n"
                                    "background:none;\n"
                                    "border: none;\n"
                                    "background-repeat: none;\n"
                                    "height:" + str(bottom_btn_height) + "px;\n"
                                    "width:" + str(btn_width) + "px;\n"
                                    "text-align: bottom;\n"
                                    "font-size: " + str(btn_text) + "px;\n"
                                    "image: url(images/thumb_210.png);\n"
                                    "font-weight: bold;\n"
                                    "padding-bottom: " + str(padding) + "px;\n"
                                    "padding-top: 0px;\n"
                                    "background-color: rgba(3, 39, 50,0.8);\n" 
                                    "border-radius:30px;\n"
                                    "margin: " + str(margin) + "px;\n"
                                    "margin-bottom: 0px;\n"
                                    "font-family: Arial, Helvetica, sans-serif;\n"
                                    "color:White;}")
            self.btn11.setStyleSheet("#btn11{\n"
                                    "background:none;\n"
                                    "border: none;\n"
                                    "background-repeat: none;\n"
                                    "height:" + str(bottom_btn_height) + "px;\n"
                                    "width:" + str(btn_width) + "px;\n"
                                    "text-align: bottom;\n"
                                    "font-size: " + str(btn_text) + "px;\n"
                                    "image: url(images/thumb_211.png);\n"
                                    "font-weight: bold;\n"
                                    "padding-bottom: " + str(padding) + "px;\n"
                                    "padding-top: 0px;\n"
                                    "background-color: rgba(3, 39, 50,0.8);\n" 
                                    "border-radius:30px;\n"
                                    "margin: " + str(margin) + "px;\n"
                                    "margin-bottom: 0px;\n"
                                    "font-family: Arial, Helvetica, sans-serif;\n"
                                    "color:White;}")
            self.btn12.setStyleSheet("#btn12{\n"
                                    "background:none;\n"
                                    "border: none;\n"
                                    "background-repeat: none;\n"
                                    "height:" + str(bottom_btn_height) + "px;\n"
                                    "width:" + str(btn_width) + "px;\n"
                                    "text-align: bottom;\n"
                                    "font-size: " + str(btn_text) + "px;\n"
                                    "image: url(images/thumb_211.png);\n"
                                    "font-weight: bold;\n"
                                    "padding-bottom: " + str(padding) + "px;\n"
                                    "padding-top: 0px;\n"
                                    "background-color: rgba(3, 39, 50,0.8);\n" 
                                    "border-radius:30px;\n"
                                    "margin: " + str(margin) + "px;\n"
                                    "margin-bottom: 0px;\n"
                                    "font-family: Arial, Helvetica, sans-serif;\n"
                                    "color:White;}")



            self.label.setStyleSheet("background-color:rgba(255,255,255,0.4);\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(bottom_btn_height) + "px;\n"
                                     "width:" + str(btn_width) + "px;\n"
                                     "padding-bottom: " + str(padding) + "px;\n"
                                     "padding-top: 0px;\n"
                                     "border-radius:30px;\n"
                                     "margin: " + str(margin) + "px;\n"
                                     "margin-bottom: 0px;")

            self.label_2.setStyleSheet("background-color:rgba(255,255,255,0.4);\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(bottom_btn_height) + "px;\n"
                                     "width:" + str(btn_width) + "px;\n"
                                     "padding-bottom: " + str(padding) + "px;\n"
                                     "padding-top: 0px;\n"
                                     "border-radius:30px;\n"
                                     "margin: " + str(margin) + "px;\n"
                                     "margin-bottom: 0px;")

            self.label_3.setStyleSheet("background-color:rgba(255,255,255,0.4);\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(bottom_btn_height) + "px;\n"
                                     "width:" + str(btn_width) + "px;\n"
                                     "padding-bottom: " + str(padding) + "px;\n"
                                     "padding-top: 0px;\n"
                                     "border-radius:30px;\n"
                                     "margin: " + str(margin) + "px;\n"
                                     "margin-bottom: 0px;")

            self.label_4.setStyleSheet("background-color:rgba(255,255,255,0.4);\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(bottom_btn_height) + "px;\n"
                                     "width:" + str(btn_width) + "px;\n"
                                     "padding-bottom: " + str(padding) + "px;\n"
                                     "padding-top: 0px;\n"
                                     "border-radius:30px;\n"
                                     "margin: " + str(margin) + "px;\n"
                                     "margin-bottom: 0px;")


            self.toggle_State =1

        elif (self.toggle_State==1):
            self.background.setStyleSheet("image: url(images/Background.png);")
            self.backFirstRow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-radius:15px;")
            for i in range (1,9):
                self.changeImg(i,i)
            self.btn9.setStyleSheet("#btn9{\n"
                                    "background:none;\n"
                                    "border: 1px solid #3FA796;\n"
                                    "background-repeat: none;\n"
                                    "height:" + str(bottom_btn_height) + "px;\n"
                                    "width:" + str(btn_width) + "px;\n"
                                    "text-align: bottom;\n"
                                    "font-size: " + str(btn_text) + "px;\n"
                                    "image: url(images/thumb_9.png);\n"
                                    "font-weight: bold;\n"
                                    "padding-bottom: " + str(padding) + "px;\n"
                                    "padding-top: 0px;\n"
                                    "background-color: " +buttonPadcolor+ ";\n" 
                                    "border-radius:30px;\n"
                                    "margin: " + str(margin) + "px;\n"
                                    "margin-bottom: 0px;\n"
                                    "font-family: Arial, Helvetica, sans-serif;\n"
                                    "color:Black;}")

            self.btn10.setStyleSheet("#btn10{\n"
                                    "background:none;\n"
                                    "border: 1px solid #3FA796;\n"
                                    "background-repeat: none;\n"
                                    "height:" + str(bottom_btn_height) + "px;\n"
                                    "width:" + str(btn_width) + "px;\n"
                                    "text-align: bottom;\n"
                                    "font-size: " + str(btn_text) + "px;\n"
                                    "image: url(images/thumb_10.png);\n"
                                    "font-weight: bold;\n"
                                    "padding-bottom: " + str(padding) + "px;\n"
                                    "padding-top: 0px;\n"
                                    "background-color: " +buttonPadcolor+ ";\n" 
                                    "border-radius:30px;\n"
                                    "margin: " + str(margin) + "px;\n"
                                    "margin-bottom: 0px;\n"
                                    "font-family: Arial, Helvetica, sans-serif;\n"
                                    "color:Black;}")

            self.btn11.setStyleSheet("#btn11{\n"
                                    "background:none;\n"
                                    "border: 1px solid #3FA796;\n"
                                    "background-repeat: none;\n"
                                    "height:" + str(bottom_btn_height) + "px;\n"
                                    "width:" + str(btn_width) + "px;\n"
                                    "text-align: bottom;\n"
                                    "font-size: " + str(btn_text) + "px;\n"
                                    "image: url(images/thumb_11.png);\n"
                                    "font-weight: bold;\n"
                                    "padding-bottom: " + str(padding) + "px;\n"
                                    "padding-top: 0px;\n"
                                    "background-color: " +buttonPadcolor+ ";\n" 
                                    "border-radius:30px;\n"
                                    "margin: " + str(margin) + "px;\n"
                                    "margin-bottom: 0px;\n"
                                    "font-family: Arial, Helvetica, sans-serif;\n"
                                    "color:Black;}")

            self.btn12.setStyleSheet("#btn12{\n"
                                    "background:none;\n"
                                    "border: 1px solid #3FA796;\n"
                                    "background-repeat: none;\n"
                                    "height:" + str(bottom_btn_height) + "px;\n"
                                    "width:" + str(btn_width) + "px;\n"
                                    "text-align: bottom;\n"
                                    "font-size: " + str(btn_text) + "px;\n"
                                    "image: url(images/thumb_12.png);\n"
                                    "font-weight: bold;\n"
                                    "padding-bottom: " + str(padding) + "px;\n"
                                    "padding-top: 0px;\n"
                                    "background-color: " +buttonPadcolor+ ";\n" 
                                    "border-radius:30px;\n"
                                    "margin: " + str(margin) + "px;\n"
                                    "margin-bottom: 0px;\n"
                                    "font-family: Arial, Helvetica, sans-serif;\n"
                                    "color:Black;}")

            self.label.setStyleSheet("background-color:transparent;\n"
                                     "border: none;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(bottom_btn_height) + "px;\n"
                                     "width:" + str(btn_width) + "px;\n"
                                     "padding-bottom: " + str(padding) + "px;\n"
                                     "padding-top: 0px;\n"
                                     "border-radius:30px;\n"
                                     "margin: " + str(margin) + "px;\n"
                                     "margin-bottom: 0px;")
            self.label_2.setStyleSheet("background-color:transparent;\n"
                                     "border: none;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(bottom_btn_height) + "px;\n"
                                     "width:" + str(btn_width) + "px;\n"
                                     "padding-bottom: " + str(padding) + "px;\n"
                                     "padding-top: 0px;\n"
                                     "border-radius:30px;\n"
                                     "margin: " + str(margin) + "px;\n"
                                     "margin-bottom: 0px;")
            self.label_3.setStyleSheet("background-color:transparent;\n"
                                     "border: none;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(bottom_btn_height) + "px;\n"
                                     "width:" + str(btn_width) + "px;\n"
                                     "padding-bottom: " + str(padding) + "px;\n"
                                     "padding-top: 0px;\n"
                                     "border-radius:30px;\n"
                                     "margin: " + str(margin) + "px;\n"
                                     "margin-bottom: 0px;")
            self.label_4.setStyleSheet("background-color:transparent;\n"
                                     "border: none;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(bottom_btn_height) + "px;\n"
                                     "width:" + str(btn_width) + "px;\n"
                                     "padding-bottom: " + str(padding) + "px;\n"
                                     "padding-top: 0px;\n"
                                     "border-radius:30px;\n"
                                     "margin: " + str(margin) + "px;\n"
                                     "margin-bottom: 0px;")
            self.toggle_State = 0


    def toggleAnimation(self):
        self.animation = QPropertyAnimation(self.toglabel,b'pos')
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(200)
        if self.toggle_State ==0:
            self.animation.setEndValue(QPoint(int(width/2+5), int(Starting_point_y-94)))
            self.toggleBtn.setStyleSheet("width:100px;\n"
                                         "height:50px;\n"
                                         "border-radius:20px;\n"
                                         "background: transparent;\n"
                                         "border: 2.5px solid white;")
            self.toggleBtn.setObjectName("pushButton")
            self.toglabel.setStyleSheet("hieght:50px;\n"
                                     "width:50px;\n"
                                     "background-color:white;\n"
                                     "border-radius:15px;")
        elif self.toggle_State ==1:
            self.animation.setEndValue(QPoint(int(width/2-45), int(Starting_point_y-94)))
            self.toggleBtn.setStyleSheet("width:100px;\n"
                                     "height:50px;\n"
                                     "border-radius:20px;\n"
                                     "background: #3CCF4E;\n"
                                     # "border: 2.5px solid grey;"
                                     "border: none;")
            self.toggleBtn.setObjectName("pushButton")
            self.toglabel.setStyleSheet("hieght:50px;\n"
                                     "width:50px;\n"
                                     "background-color:white;\n"
                                     "border-radius:15px;")
            self.toggleBtn.setObjectName("pushButton")

        self.animation.start()


    def clicked_btn(self, val):
        if ((val >= 9)and(val <= 12)):
            self.secondWindow = QtWidgets.QMainWindow()
            self.ui = Ui_secondWindow()
            self.ui.buttonVal = val
            self.ui.toggle_State =self.toggle_State
            self.ui.setupUi(self.secondWindow)
            self.secondWindow.show()
        else:
            if (self.btn_state[val-1]==0):
                self.changeImg(val,30+val)
                self.btn_state[val - 1] = 1
            else:
                if (self.toggle_State==0):
                    self.changeImg(val, val)
                elif (self.toggle_State==1):
                    self.changeImg(val, 20+val)
                self.btn_state[val - 1] = 0


    def ThreadOpen(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.IsWiFi.connect(self.WiFi_Connected)
        self.worker.IsBlue.connect(self.BlueT_Connected)
        self.worker.timeNow.connect(self.update_Time)

    def update_Time(self,val):
          self.timeDis.setText(val)

    def WiFi_Connected(self,val):
        if val:
            self.wifi.setStyleSheet("image: url(images/wifi_connected.png);")
        else:
            self.wifi.setStyleSheet("image: url(images/wifi_disconnected.png);")

    def BlueT_Connected(self,val):
        if val:
            self.Bluetooth.setStyleSheet("image: url(images/bluetooth_connected.png);")
        else:
            self.Bluetooth.setStyleSheet("image: url(images/bluetooth_disconnected.png);")

    def changeImg(self,btn_no,img_no):
        if (img_no!=0):
            if btn_no==1:
                self.btn1.setStyleSheet("#btn"+str(btn_no)+"{\n"
                                     "background:none;\n"
                                     "border: none;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(top_btn_height) + "px;\n"
                                                                          "text-align: bottom;\n"
                                                                          "font-size: 30px;\n"
                                                                          "image: url(images/thumb_"+str(img_no)+".png);\n"
                                                                          "font-weight: bold;\n"
                                                                          "font-family: Arial, Helvetica, sans-serif;\n"
                                                                          "color:#2C3333;}\n"
                                                                          "")
            if btn_no==2:
                self.btn2.setStyleSheet("#btn"+str(btn_no)+"{\n"
                                     "background:none;\n"
                                     "border: none;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(top_btn_height) + "px;\n"
                                                                          "text-align: bottom;\n"
                                                                          "font-size: 30px;\n"
                                                                          "image: url(images/thumb_"+str(img_no)+".png);\n"
                                                                          "font-weight: bold;\n"
                                                                          "font-family: Arial, Helvetica, sans-serif;\n"
                                                                          "color:#2C3333;}\n"
                                                                          "")
            if btn_no==3:
                self.btn3.setStyleSheet("#btn"+str(btn_no)+"{\n"
                                     "background:none;\n"
                                     "border: none;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(top_btn_height) + "px;\n"
                                                                          "text-align: bottom;\n"
                                                                          "font-size: 30px;\n"
                                                                          "image: url(images/thumb_"+str(img_no)+".png);\n"
                                                                          "font-weight: bold;\n"
                                                                          "font-family: Arial, Helvetica, sans-serif;\n"
                                                                          "color:#2C3333;}\n"
                                                                          "")
            if btn_no==4:
                self.btn4.setStyleSheet("#btn"+str(btn_no)+"{\n"
                                     "background:none;\n"
                                     "border: none;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(top_btn_height) + "px;\n"
                                                                          "text-align: bottom;\n"
                                                                          "font-size: 30px;\n"
                                                                          "image: url(images/thumb_"+str(img_no)+".png);\n"
                                                                          "font-weight: bold;\n"
                                                                          "font-family: Arial, Helvetica, sans-serif;\n"
                                                                          "color:#2C3333;}\n"
                                                                          "")
            if btn_no==5:
                self.btn5.setStyleSheet("#btn"+str(btn_no)+"{\n"
                                     "background:none;\n"
                                     "border: none;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(top_btn_height) + "px;\n"
                                                                          "text-align: bottom;\n"
                                                                          "font-size: 30px;\n"
                                                                          "image: url(images/thumb_"+str(img_no)+".png);\n"
                                                                          "font-weight: bold;\n"
                                                                          "font-family: Arial, Helvetica, sans-serif;\n"
                                                                          "color:#2C3333;}\n"
                                                                          "")
            # if btn_no==6:
            #     self.btn6.setStyleSheet("#btn"+str(btn_no)+"{\n"
            #                          "background:none;\n"
            #                          "border: none;\n"
            #                          "background-repeat: none;\n"
            #                          "height:" + str(top_btn_height) + "px;\n"
            #                                                               "text-align: bottom;\n"
            #                                                               "font-size: 30px;\n"
            #                                                               "image: url(images/thumb_"+str(img_no)+".png);\n"
            #                                                               "font-weight: bold;\n"
            #                                                               "font-family: Arial, Helvetica, sans-serif;\n"
            #                                                               "color:#2C3333;}\n"
            #                                                               "")
            # if btn_no==7:
            #     self.btn7.setStyleSheet("#btn"+str(btn_no)+"{\n"
            #                          "background:none;\n"
            #                          "border: none;\n"
            #                          "background-repeat: none;\n"
            #                          "height:" + str(top_btn_height) + "px;\n"
            #                                                               "text-align: bottom;\n"
            #                                                               "font-size: 30px;\n"
            #                                                               "image: url(images/thumb_"+str(img_no)+".png);\n"
            #                                                               "font-weight: bold;\n"
            #                                                               "font-family: Arial, Helvetica, sans-serif;\n"
            #                                                               "color:#2C3333;}\n"
            #                                                               "")
            # if btn_no==8:
            #     self.btn8.setStyleSheet("#btn"+str(btn_no)+"{\n"
            #                          "background:none;\n"
            #                          "border: none;\n"
            #                          "background-repeat: none;\n"
            #                          "height:" + str(top_btn_height) + "px;\n"
            #                                                               "text-align: bottom;\n"
            #                                                               "font-size: 30px;\n"
            #                                                               "image: url(images/thumb_"+str(img_no)+".png);\n"
            #                                                               "font-weight: bold;\n"
            #                                                               "font-family: Arial, Helvetica, sans-serif;\n"
            #                                                               "color:#2C3333;}\n"
            #                                                               "")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
