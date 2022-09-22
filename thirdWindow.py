from datetime import datetime
from PyQt5 import QtCore, QtWidgets
import pyautogui
from Thread import WorkerThread


class Ui_thirdWindow(object):

    buttonVal =0
    toggle_State = 0

    def setupUi(self, thirdWindow):
        global bat_start, bat_len, thumbail, thumbnail, background_Img, btnPadColor, border, btnTextColor
        thirdWindow.setObjectName("thirdWindow")
        width, height = pyautogui.size()

        # width = 1437
        # height =900

        icon_width = int(width/3)
        icon_font_height = int(height/30)

        thirdWindow.resize(width, height)
        thirdWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(thirdWindow)
        self.centralwidget.setObjectName("centralwidget")



        # self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(int((width/8)*2), int((height/12)*3), int((width/8)*4), int((height/12)*6)))
        # self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # self.BtnCol = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        # self.BtnCol.setContentsMargins(0, 0, 0, 0)
        # self.BtnCol.setObjectName("verticalLayoutWidget")
        #
        #
        # self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label.setObjectName("label")
        # self.BtnCol.addWidget(self.label)
        #
        # self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label_2.setObjectName("label_2")
        # self.BtnCol.addWidget(self.label_2)
        #
        # self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label_3.setObjectName("label_3")
        # self.BtnCol.addWidget(self.label_3)
        #
        # self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label_4.setObjectName("label_4")
        # self.BtnCol.addWidget(self.label_4)


        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, width,height))

        if (self.toggle_State==0):
            self.background.setStyleSheet("image: url(images/Background.png);")
            thumbnail = "thumb_" + str(self.buttonVal)
            btnPadColor = "White"
            btnTextColor = "Black"
            border = "1px solid #3FA796"
            # self.label.setStyleSheet("background-color:transparent;\n"
            #                          "background-repeat: none;\n"
            #                          "width:" + str(icon_width) + "px;\n"
            #                          "height:" + str(icon_height) + "px;\n"
            #                          "border:none;\n"
            #                          "border-radius:10px;")
            # self.label_2.setStyleSheet("background-color:transparent;\n"
            #                          "background-repeat: none;\n"
            #                          "width:" + str(icon_width) + "px;\n"
            #                          "height:" + str(icon_height) + "px;\n"
            #                          "border:none;\n"
            #                          "border-radius:10px;")
            # self.label_3.setStyleSheet("background-color:transparent;\n"
            #                          "background-repeat: none;\n"
            #                          "width:" + str(icon_width) + "px;\n"
            #                          "height:" + str(icon_height) + "px;\n"
            #                          "border:none;\n"
            #                          "border-radius:10px;")
            # self.label_4.setStyleSheet("background-color:transparent;\n"
            #                          "background-repeat: none;\n"
            #                          "width:" + str(icon_width) + "px;\n"
            #                          "height:" + str(icon_height) + "px;\n"
            #                          "border:none;\n"
            #                          "border-radius:10px;")


        elif (self.toggle_State==1):
            self.background.setStyleSheet("image: url(images/Background_D.png);")
            btnPadColor = "rgba(3, 39, 50,0.8)"
            btnTextColor = "White"
            border = "none"
            if  self.buttonVal==9:
                thumbnail = "thumb_20" + str(self.buttonVal)
            else:
                thumbnail = "thumb_2" + str(self.buttonVal)
            # self.label.setStyleSheet("background-color:rgba(255,255,255,0.4);\n"
            #                          "background-repeat: none;\n"
            #                          "width:" + str(icon_width) + "px;\n"
            #                          "height:" + str(icon_height) + "px;\n"
            #                          "border:none;\n"
            #                          "border-radius:10px;")
            # self.label_2.setStyleSheet("background-color:rgba(255,255,255,0.4);\n"
            #                          "background-repeat: none;\n"
            #                          "width:" + str(icon_width) + "px;\n"
            #                          "height:" + str(icon_height) + "px;\n"
            #                          "border:none;\n"
            #                          "border-radius:10px;")
            # self.label_3.setStyleSheet("background-color:rgba(255,255,255,0.4);\n"
            #                          "background-repeat: none;\n"
            #                          "width:" + str(icon_width) + "px;\n"
            #                          "height:" + str(icon_height) + "px;\n"
            #                          "border:none;\n"
            #                          "border-radius:10px;")
            # self.label_4.setStyleSheet("background-color:rgba(255,255,255,0.4);\n"
            #                          "background-repeat: none;\n"
            #                          "width:" + str(icon_width) + "px;\n"
            #                          "height:" + str(icon_height) + "px;\n"
            #                          "border:none;\n"
            #                          "border-radius:10px;")

        self.background.setText("")
        self.background.setScaledContents(True)
        self.background.setObjectName("Background")




        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, int(height/12), width, int(height/12)*2))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.IconBar = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.IconBar.setContentsMargins(0, 0, 0, 0)
        self.IconBar.setObjectName("IconBar")


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


        thirdWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(thirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        thirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(thirdWindow)
        self.statusbar.setObjectName("statusbar")
        thirdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(thirdWindow)
        QtCore.QMetaObject.connectSlotsByName(thirdWindow)



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


        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(int((width/8)*2), int((height/12)*3), int((width/8)*4), int((height/12)*6)))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout_2")


        self.btn1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn1.setText("Option1")
        self.btn1.setStyleSheet("width:" + str(icon_width) + "px;\n"
                                "height:" + str(icon_height) + "px;\n"
                                "background:"+btnPadColor+";\n"
                                "border:"+border+";\n" 
                                "font-size:"+ str(icon_font_height) +"px;\n"
                                "border-radius:10px;\n"
                                "font-weight: bold;\n"
                                "font-family: Arial, Helvetica, sans-serif;\n"
                                "color:"+btnTextColor+";")
        self.btn1.setObjectName("btn1")
        self.verticalLayout.addWidget(self.btn1)


        self.btn2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn2.setText("Option2")
        self.btn2.setStyleSheet("width:" + str(icon_width) + "px;\n"
                                "height:" + str(icon_height) + "px;\n"
                                "background:"+btnPadColor+";\n"
                                "border:"+border+";\n"        
                                "font-size:"+ str(icon_font_height) +"px;\n"
                                "border-radius:10px;\n"
                                "font-weight: bold;\n"
                                "font-family: Arial, Helvetica, sans-serif;\n"
                                "color:"+btnTextColor+";")
        self.btn2.setObjectName("btn2")
        self.verticalLayout.addWidget(self.btn2)

        self.btn3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn3.setText("Option3")
        self.btn3.setStyleSheet("width:" + str(icon_width) + "px;\n"
                                "height:" + str(icon_height) + "px;\n"
                                "background:"+btnPadColor+";\n"
                                "border:"+border+";\n" 
                                "font-size:"+ str(icon_font_height) +"px;\n"
                                "border-radius:10px;\n"
                                "font-weight: bold;\n"
                                "font-family: Arial, Helvetica, sans-serif;\n"
                                "color:"+btnTextColor+";")
        self.btn3.setObjectName("btn3")
        self.verticalLayout.addWidget(self.btn3)


        self.btn4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn4.setText("Option4")
        self.btn4.setStyleSheet("width:" + str(icon_width) + "px;\n"
                                "height:" + str(icon_height) + "px;\n"
                                "background:"+btnPadColor+";\n"
                                "border:"+border+";\n" 
                                "font-size:"+ str(icon_font_height) +"px;\n"
                                "border-radius:10px;\n"
                                "font-weight: bold;\n"
                                "font-family: Arial, Helvetica, sans-serif;\n"
                                "color:"+btnTextColor+";")
        self.btn4.setObjectName("btn4")
        self.verticalLayout.addWidget(self.btn4)


        # self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()

        self.backBtn.clicked.connect(thirdWindow.close)



    def retranslateUi(self, thirdWindow):
        _translate = QtCore.QCoreApplication.translate
        thirdWindow.setWindowTitle(_translate("thirdWindow", "MainWindow"))


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
    thirdWindow = QtWidgets.QMainWindow()
    ui = Ui_thirdWindow()
    ui.setupUi(thirdWindow)
    thirdWindow.show()
    sys.exit(app.exec())