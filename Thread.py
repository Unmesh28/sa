import bluetooth
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from datetime import datetime

class WorkerThread (QThread):

    timeNow = pyqtSignal(str)
    IsWiFi = pyqtSignal(bool)
    IsBlue = pyqtSignal(bool)
    # batVal = pyqtSignal(int)

    def run(self):
        while (True):
            # val = psutil.sensors_battery().percent
            # self.batVal.emit(val)
            nowtime = datetime.now()
            current_time = nowtime.strftime("%H:%M")
            self.timeNow.emit(current_time)
            try:
                devices = bluetooth.discover_devices(lookup_names=True)
                number_of_devices = len(devices)
                if (number_of_devices == 0):
                    self.IsBlue.emit(False)
                else:
                    self.IsBlue.emit(True)

                url = "http://www.google.com"
                timeout = 5
                try:
                    request = requests.get(url, timeout=timeout)
                    self.IsWiFi.emit(True)
                    # print("Connected to the Internet")
                except (requests.ConnectionError, requests.Timeout) as exception:
                    self.IsWiFi.emit(False)
                    # print("No internet connection.")
            except:
                self.IsBlue.emit(False)





