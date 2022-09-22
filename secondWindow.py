from datetime import datetime
from PyQt5 import QtCore, QtWidgets
import pyautogui
from PyQt5.QtWidgets import QGraphicsBlurEffect

from thirdWindow import Ui_thirdWindow
from Thread import WorkerThread
from collision_warning import func



class Ui_secondWindow(object):

    buttonVal =0
    toggle_State = 0

    def setupUi(self, secondWindow):
        global bat_start, bat_len, thumbail, thumbnail, btn_width, margin, bottom_btn_height, fac1, fac2, background_Img,btnPadColor,btnTextColor,border
        secondWindow.setObjectName("secondWindow")
        width, height = pyautogui.size()

        # width = 1437
        # height =900

        margin = int((width / 16))
        top_btn_height = int(height / 12)

        if width >1800:
            margin = margin = int((width / 20))
            bottom_btn_height = int(top_btn_height * 6)
            fac1 = 4
            fac2 = 8

        if width <1800:
            margin = margin = int((width / 16))
            bottom_btn_height = int(top_btn_height * 7)
            fac1 = 3
            fac2 = 10

        btn_width = int(width / 12)
        Starting_point_y = int((width / 10) * 1.2)
        padding = int(width/48)
        font_size = int (height/45)
        border_radius = int(height/35)


        secondWindow.resize(width, height)
        secondWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(secondWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(int((width/16)*fac1), int(Starting_point_y), int((width/16)*fac2), int(bottom_btn_height)))
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

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, width,height))

        if (self.toggle_State==0):
            self.background.setStyleSheet("image: url(images/Background.png);")
            thumbnail = "thumb_" + str(self.buttonVal)
            btnPadColor = "White"
            btnTextColor = "Black"
            border = "1px solid #3FA796"
            self.label.setStyleSheet("background-color:transparent;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(bottom_btn_height) + "px;\n"
                                     "width:" + str(btn_width) + "px;\n"
                                     "padding-bottom: " + str(padding) + "px;\n"
                                     "padding-top: 0px;\n"
                                     "border-radius:30px;\n"
                                     "margin: " + str(margin) + "px;\n"
                                     "margin-bottom: 0px;")

            self.label_2.setStyleSheet("background-color:transparent;\n"
                                     "background-repeat: none;\n"
                                     "height:" + str(bottom_btn_height) + "px;\n"
                                     "width:" + str(btn_width) + "px;\n"
                                     "padding-bottom: " + str(padding) + "px;\n"
                                     "padding-top: 0px;\n"
                                     "border-radius:30px;\n"
                                     "margin: " + str(margin) + "px;\n"
                                     "margin-bottom: 0px;")
        elif (self.toggle_State==1):
            self.background.setStyleSheet("image: url(images/Background_D.png);")
            btnPadColor = "rgba(3, 39, 50,0.8)"
            btnTextColor = "White"
            border = "none"
            if  self.buttonVal==9:
                thumbnail = "thumb_20" + str(self.buttonVal)
            else:
                thumbnail = "thumb_2" + str(self.buttonVal)
            self.label.setStyleSheet("width:" + str(btn_width) + "px;\n"
                                "height:" + str(bottom_btn_height) + "px;\n"
                                "border:"+border+";\n"
                                "background-color:rgba(255,255,255,0.4);\n"
                                "margin:" + str(margin) + "px;\n"
                                "padding:" + str(padding) + "px;\n"
                                "border-radius:" + str(border_radius) + "px;")
            self.label_2.setStyleSheet("width:" + str(btn_width) + "px;\n"
                                "height:" + str(bottom_btn_height) + "px;\n"
                                "border:"+border+";\n"
                                "background-color:rgba(255,255,255,0.4);\n"
                                "margin:" + str(margin) + "px;\n"
                                "padding:" + str(padding) + "px;\n"
                                "border-radius:" + str(border_radius) + "px;")

        print(self.toggle_State)
        self.background.setText("")
        self.background.setScaledContents(True)
        self.background.setObjectName("Background")





        icon_height = int (height/15)

        self.Icon = QtWidgets.QLabel(self.centralwidget)
        self.Icon.setGeometry(QtCore.QRect(int((width/35)), int(height/8), icon_height, icon_height))
        self.Icon.setStyleSheet("image: url(images/"+thumbnail+ ".png);\n"
                                 "height: "+str(icon_height)+ "px;\n"
                                "width:"+str(icon_height)+ "px;")
        self.Icon.setScaledContents(True)
        self.Icon.setObjectName("label")


        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(int((width/16)*14.7), int(height/12),int(width/16), int(height/12)*2))
        self.backBtn.setText("Back")
        self.backBtn.setStyleSheet("background-color:transparent;\n"
                                           "background:none;\n"
                                           "border:none;\n"
                                           "background-repeat:none;\n"
        "height: 50px;\n"
        "width:50px;\n"
        "text-align: centre;\n"
        "font-size: 25px;\n"
        "font-weight: bold;\n"
        "font-family: Arial, Helvetica, sans-serif;\n"
        "color:#FFFFFF;")
        self.backBtn.setObjectName("backBtn")



        secondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(secondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        secondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(secondWindow)
        self.statusbar.setObjectName("statusbar")
        secondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(secondWindow)
        QtCore.QMetaObject.connectSlotsByName(secondWindow)

        self.ThreadOpen()


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


        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(int((width/16)*fac1), int(Starting_point_y), int((width/16)*fac2), int(bottom_btn_height)))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn1.setText("Settings")
        self.btn1.setStyleSheet("width:" + str(btn_width) + "px;\n"
                                "height:" + str(bottom_btn_height) + "px;\n"
                                "border:"+border+";\n"
                                "background:"+btnPadColor+";\n"
                                "margin:" + str(margin) + "px;\n"
                                "padding:" + str(padding) + "px;\n"
                                "border-radius:" + str(border_radius) + "px;\n"
                                "text-align:bottom;\n"
                                "font-size:" + str(font_size) + "px;\n"
                                "font-weight: bold;\n"
                                "font-family: Arial, Helvetica, sans-serif;\n"
                                "color:"+btnTextColor+";\n"
                                "image: url(images/icon_1.png);\n"
                                "")
        self.btn1.setObjectName("btn1")




        self.horizontalLayout.addWidget(self.btn1)
        self.btn1.clicked.connect(self.callCollisionCode)

        self.btn2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn2.setText("Monitor")
        self.btn2.setStyleSheet("width:" + str(btn_width) + "px;\n"
                                "border:"+border+";\n"
                                "height:" + str(bottom_btn_height) + "px;\n"
                                "background:"+btnPadColor+";\n"
                                "margin:" + str(margin) + "px;\n"
                                "padding:" + str(padding) + "px;\n"
                                "border-radius:" + str(border_radius) + "px;\n"
                                "text-align:bottom;\n"
                                "font-size:" + str(font_size) + "px;\n"
                                "font-weight: bold;\n"
                                "font-family: Arial, Helvetica, sans-serif;\n"
                                "color:"+btnTextColor+";\n"
                                "image: url(images/icon_2.png);")
        self.btn2.setObjectName("btn2")
        self.horizontalLayout.addWidget(self.btn2)
        self.btn2.clicked.connect(self.clicked_btn)



        self.horizontalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget.raise_()


        self.backBtn.clicked.connect(secondWindow.close)



    def callCollisionCode():
        func()


    def retranslateUi(self, secondWindow):
        _translate = QtCore.QCoreApplication.translate
        secondWindow.setWindowTitle(_translate("secondWindow", "MainWindow"))

    def clicked_btn(self):
        self.thirdwindow = QtWidgets.QMainWindow()
        self.third = Ui_thirdWindow()
        self.third.buttonVal = self.buttonVal
        self.third.toggle_State = self.toggle_State
        self.third.setupUi(self.thirdwindow)
        self.thirdwindow.show()


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




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    secondWindow = QtWidgets.QMainWindow()
    ui = Ui_secondWindow()
    ui.setupUi(secondWindow)
    secondWindow.show()
    sys.exit(app.exec())