# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Weather(object):
    def setupUi(self, Weather):
        Weather.setObjectName("Weather")
        Weather.resize(200, 200)
        Weather.setMinimumSize(QtCore.QSize(200, 200))
        Weather.setMaximumSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(Weather)
        self.centralwidget.setObjectName("centralwidget")
        self.enter_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_label.setGeometry(QtCore.QRect(10, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.enter_label.setFont(font)
        self.enter_label.setObjectName("enter_label")
        self.city_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.city_entry.setGeometry(QtCore.QRect(80, 110, 71, 20))
        self.city_entry.setObjectName("city_entry")
        self.enter_button = QtWidgets.QPushButton(self.centralwidget)
        self.enter_button.setGeometry(QtCore.QRect(150, 110, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setObjectName("enter_button")
        self.weather_des = QtWidgets.QLabel(self.centralwidget)
        self.weather_des.setGeometry(QtCore.QRect(10, 0, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.weather_des.setFont(font)
        self.weather_des.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_des.setWordWrap(True)
        self.weather_des.setObjectName("weather_des")
        self.temp_numF = QtWidgets.QLabel(self.centralwidget)
        self.temp_numF.setGeometry(QtCore.QRect(20, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.temp_numF.setFont(font)
        self.temp_numF.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_numF.setObjectName("temp_numF")
        self.celsius_label = QtWidgets.QLabel(self.centralwidget)
        self.celsius_label.setGeometry(QtCore.QRect(150, 50, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.celsius_label.setFont(font)
        self.celsius_label.setAlignment(QtCore.Qt.AlignCenter)
        self.celsius_label.setObjectName("celsius_label")
        self.farenhei_label = QtWidgets.QLabel(self.centralwidget)
        self.farenhei_label.setGeometry(QtCore.QRect(60, 50, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.farenhei_label.setFont(font)
        self.farenhei_label.setAlignment(QtCore.Qt.AlignCenter)
        self.farenhei_label.setObjectName("farenhei_label")
        self.temp_numC = QtWidgets.QLabel(self.centralwidget)
        self.temp_numC.setGeometry(QtCore.QRect(110, 60, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.temp_numC.setFont(font)
        self.temp_numC.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_numC.setObjectName("temp_numC")
        self.error_thing = QtWidgets.QLabel(self.centralwidget)
        self.error_thing.setGeometry(QtCore.QRect(10, 20, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.error_thing.setFont(font)
        self.error_thing.setAlignment(QtCore.Qt.AlignCenter)
        self.error_thing.setObjectName("error_thing")
        Weather.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Weather)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        Weather.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Weather)
        self.statusbar.setObjectName("statusbar")
        Weather.setStatusBar(self.statusbar)

        self.retranslateUi(Weather)
        QtCore.QMetaObject.connectSlotsByName(Weather)

    def retranslateUi(self, Weather):
        _translate = QtCore.QCoreApplication.translate
        Weather.setWindowTitle(_translate("Weather", "Weather"))
        self.enter_label.setText(_translate("Weather", "Enter City:"))
        self.enter_button.setText(_translate("Weather", "Go"))
        self.weather_des.setText(_translate("Weather", "Description"))
        self.temp_numF.setText(_translate("Weather", "XX"))
        self.celsius_label.setText(_translate("Weather", "C"))
        self.farenhei_label.setText(_translate("Weather", "F"))
        self.temp_numC.setText(_translate("Weather", "XX"))
        self.error_thing.setText(_translate("Weather", "Invalid City Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Weather = QtWidgets.QMainWindow()
    ui = Ui_Weather()
    ui.setupUi(Weather)
    Weather.show()
    sys.exit(app.exec_())