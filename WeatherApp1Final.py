# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: Jenson Jones using PyQt5 UI code generator 5.15.0

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap 
from PyQt5.QtCore import QTime
from datetime import datetime, date
from pytz import timezone
from pyzipcode import ZipCodeDatabase
import pytz


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 338)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.zipCodeSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.zipCodeSearch.setGeometry(QtCore.QRect(540, 10, 111, 21))
        self.zipCodeSearch.setObjectName("zipCodeSearch")

        self.clockLabel = QtWidgets.QLabel(self.centralwidget)
        self.clockLabel.setEnabled(True)
        self.clockLabel.setGeometry(QtCore.QRect(10, 0, 311, 31))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.clockLabel.setFont(font)
        self.clockLabel.setAutoFillBackground(False)
        self.clockLabel.setStyleSheet("")
        self.clockLabel.setObjectName("clockLabel")
        
        self.zipCodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.zipCodeLabel.setGeometry(QtCore.QRect(470, 10, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zipCodeLabel.setFont(font)
        self.zipCodeLabel.setObjectName("zipCodeLabel")

        self.central_widget = QWidget()
        MainWindow.setCentralWidget(self.central_widget)
  
        self.iconLabel = QtWidgets.QLabel(self.centralwidget)
        self.iconLabel.setGeometry(QtCore.QRect(20, 60, 201, 191))
        self.iconLabel.setAutoFillBackground(False)
        self.iconLabel.setStyleSheet("")
        self.iconLabel.setText("")
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setObjectName("iconLabel")
        
        self.tempLabel = QtWidgets.QLabel(self.centralwidget)
        self.tempLabel.setGeometry(QtCore.QRect(250, 70, 241, 121))
        font = QtGui.QFont()
        font.setPointSize(150)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tempLabel.setFont(font)
        self.tempLabel.setAutoFillBackground(False)
        self.tempLabel.setStyleSheet("")
        self.tempLabel.setObjectName("tempLabel")
        
        self.conditionLabel = QtWidgets.QLabel(self.centralwidget)
        self.conditionLabel.setGeometry(QtCore.QRect(250, 200, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.conditionLabel.setFont(font)
        self.conditionLabel.setStyleSheet("")
        self.conditionLabel.setObjectName("conditionLabel")
        
        self.feelsLikeLabel = QtWidgets.QLabel(self.centralwidget)
        self.feelsLikeLabel.setGeometry(QtCore.QRect(250, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.feelsLikeLabel.setFont(font)
        self.feelsLikeLabel.setStyleSheet("")
        self.feelsLikeLabel.setObjectName("feelsLikeLabel")
        
        self.feelsLikeTemp = QtWidgets.QLabel(self.centralwidget)
        self.feelsLikeTemp.setGeometry(QtCore.QRect(360, 240, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.feelsLikeTemp.setFont(font)
        self.feelsLikeTemp.setStyleSheet("")
        self.feelsLikeTemp.setObjectName("feelsLikeTemp")
        
        self.tempHiLabel = QtWidgets.QLabel(self.centralwidget)
        self.tempHiLabel.setGeometry(QtCore.QRect(500, 80, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempHiLabel.setFont(font)
        self.tempHiLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.tempHiLabel.setObjectName("tempHiLabel")
        
        self.tempLoLabel = QtWidgets.QLabel(self.centralwidget)
        self.tempLoLabel.setGeometry(QtCore.QRect(500, 110, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempLoLabel.setFont(font)
        self.tempLoLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.tempLoLabel.setObjectName("tempLoLabel")
        
        self.humidityLabel = QtWidgets.QLabel(self.centralwidget)
        self.humidityLabel.setGeometry(QtCore.QRect(500, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.humidityLabel.setFont(font)
        self.humidityLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.humidityLabel.setObjectName("humidityLabel")
        
        self.visibilityLabel = QtWidgets.QLabel(self.centralwidget)
        self.visibilityLabel.setGeometry(QtCore.QRect(500, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.visibilityLabel.setFont(font)
        self.visibilityLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.visibilityLabel.setObjectName("visibilityLabel")
        
        self.sunriseLabel = QtWidgets.QLabel(self.centralwidget)
        self.sunriseLabel.setGeometry(QtCore.QRect(500, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sunriseLabel.setFont(font)
        self.sunriseLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.sunriseLabel.setObjectName("sunriseLabel")
        
        self.sunsetLabel = QtWidgets.QLabel(self.centralwidget)
        self.sunsetLabel.setGeometry(QtCore.QRect(500, 230, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sunsetLabel.setFont(font)
        self.sunsetLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.sunsetLabel.setObjectName("sunsetLabel")
        
        self.tempHiNum = QtWidgets.QLabel(self.centralwidget)
        self.tempHiNum.setGeometry(QtCore.QRect(530, 80, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempHiNum.setFont(font)
        self.tempHiNum.setStyleSheet("color:rgb(90, 90, 90)")
        self.tempHiNum.setObjectName("tempHiNum")
        
        self.tempLoNum = QtWidgets.QLabel(self.centralwidget)
        self.tempLoNum.setGeometry(QtCore.QRect(530, 110, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tempLoNum.setFont(font)
        self.tempLoNum.setStyleSheet("color:rgb(90, 90, 90)")
        self.tempLoNum.setObjectName("tempLoNum")
        
        self.humidityNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.humidityNumLabel.setGeometry(QtCore.QRect(595, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.humidityNumLabel.setFont(font)
        self.humidityNumLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.humidityNumLabel.setObjectName("humidityNumLabel")
        
        self.visNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.visNumLabel.setGeometry(QtCore.QRect(590, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.visNumLabel.setFont(font)
        self.visNumLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.visNumLabel.setObjectName("visNumLabel")
        
        self.sunriseNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.sunriseNumLabel.setGeometry(QtCore.QRect(580, 200, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sunriseNumLabel.setFont(font)
        self.sunriseNumLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.sunriseNumLabel.setObjectName("sunriseNumLabel")
        
        self.sunsetNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.sunsetNumLabel.setGeometry(QtCore.QRect(580, 230, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sunsetNumLabel.setFont(font)
        self.sunsetNumLabel.setAutoFillBackground(False)
        self.sunsetNumLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.sunsetNumLabel.setObjectName("sunsetNumLabel")
        
        self.zipcodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.zipcodeLabel.setGeometry(QtCore.QRect(10, 20, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.zipcodeLabel.setFont(font)
        self.zipcodeLabel.setObjectName("zipcodeLabel")

        self.locationLabel = QtWidgets.QLabel(self.centralwidget)
        self.locationLabel.setGeometry(QtCore.QRect(10, 265, 500, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setPointSize(20)
        font.setWeight(65)
        self.locationLabel.setStyleSheet("color:rgb(90, 90, 90)")
        self.locationLabel.setFont(font)
        self.locationLabel.setObjectName("locationLabel")

        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(555, 40, 100, 32)
        self.refreshButton.setText("Refresh")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #* event connect triggers 
        self.zipCodeSearch.returnPressed.connect(lambda: self.getWeather(MainWindow))
        self.refreshButton.clicked.connect(lambda: self.getWeather(MainWindow))

    def getWeather(self, MainWindow):
        import requests

        zipCode = self.zipCodeSearch.text()
        self.zipcodeLabel.setText(str(zipCode))
        self.zipcodeLabel.setStyleSheet("color:rgb(0, 0, 0)")

        try: 
            key = #* API KEY HERE (https://openweathermap.org/appid)
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=%s' % (zipCode, key))
            data = r.json()
            #print(data) <-- uncomment to see full json 
            
            self.updateGUI(data, zipCode)
        except:
            self.zipcodeLabel.setText("Error: " + data['message'])
            self.zipcodeLabel.setStyleSheet("color:rgb(200, 0, 0)")

    def getZone(self, zipcode):

        z = ZipCodeDatabase() #using pyzipcode
        code = z[zipcode]
        zone = code.timezone

        if zone == -5: #not the most efficient
            zone = pytz.timezone("US/Eastern")
        elif zone == -6:
            zone = pytz.timezone("US/Central")
        elif zone == -7:
            zone = pytz.timezone("US/Mountain")
        elif zone == -8:
            zone = pytz.timezone("US/Pacific")
        elif zone == -9:
            zone = pytz.timezone("US/Alaska")
        elif zone == -10:
            zone = pytz.timezone("US/Hawaii")

        if code.state == "AZ": 
            zone = pytz.timezone("US/Arizona")
            
        return zone

    def updateGUI(self, weatherData, zipcode):
        from pytemp import pytemp
        
        descrptMain = weatherData['weather'][0]['main'] #main description (hot, clear, cloudy, sunny, etc.)

        #*temp, highs, lows, humidity
        realKelvinTemp = weatherData['main']['temp'] #get temperature in K
        realTempF = int(pytemp(realKelvinTemp, 'kelvin', 'fahrenheit')) #convert K temperature to temperature in F
        feelsLikeKelvin = weatherData['main']['feels_like'] #same as above, but for heat index 
        feelsLike = int(pytemp(feelsLikeKelvin, 'kelvin', 'fahrenheit'))

        humid = weatherData['main']['humidity']

        hiTempKelvin = weatherData['main']['temp_max']
        hiTempF = int(pytemp(hiTempKelvin, 'kelvin', 'fahrenheit'))
        
        loTempKelvin = weatherData['main']['temp_min']
        loTempF = int(pytemp(loTempKelvin, 'kelvin', 'fahrenheit'))

        self.tempLabel.setText(str(realTempF)+'°')
        self.tempLabel.repaint()
        self.tempLabel.setGeometry(QtCore.QRect(245, 70, 241, 121)) #250 default

        self.conditionLabel.setText(descrptMain)
        self.conditionLabel.repaint()
        self.feelsLikeTemp.setText(str(feelsLike)+'°')
        self.feelsLikeTemp.repaint()
        self.tempHiNum.setText(str(hiTempF)+ '°')
        self.tempHiNum.repaint()
        self.tempLoNum.setText(str(loTempF)+'°')
        self.tempLoNum.repaint()
        self.humidityNumLabel.setText(str(humid) + '%')
        self.humidityLabel.repaint()
        
        self.visNumLabel.setText(str(int(weatherData['visibility']*0.00062137)) + ' mi')
        self.visNumLabel.repaint()

        #*sunrise/sunset time 
        
        utc = pytz.utc
        timezone = self.getZone(zipcode) 
      
        self.sunriseTimeUnix = weatherData['sys']['sunrise']
        self.sunriseReadTime = utc.localize(datetime.utcfromtimestamp(self.sunriseTimeUnix)) #use localize for dealing with timezones
        self.sunriseWithTimezone = self.sunriseReadTime.astimezone(timezone)
        self.sunriseTimeHuman = self.sunriseWithTimezone.strftime("%-I:%M") #only print out hour:minute in 12 hour format
        
        self.sunsetTimeUnix = weatherData['sys']['sunset']
        self.sunsetReadTime = utc.localize(datetime.utcfromtimestamp(self.sunsetTimeUnix))
        self.sunsetWithTimezone = self.sunsetReadTime.astimezone(timezone)
        self.sunsetTimeHuman = self.sunsetWithTimezone.strftime("%-I:%M")
       
        
        self.sunriseNumLabel.setText(self.sunriseTimeHuman + ' am')  
        self.sunriseNumLabel.repaint()
        self.sunsetNumLabel.setText(self.sunsetTimeHuman + ' pm')
        self.sunsetNumLabel.repaint()

        #*update weather Icon
        iconID = weatherData['weather'][0]['icon']
        iconFilename = iconID + '.png'

        im = QPixmap("FILE PATH HERE/weather_icons/%s" % iconFilename) #display the corresponding weather icon (provide full file path)
        self.iconLabel.setPixmap(im)
        self.iconLabel.repaint()

        #* update locationLabel (city, state)
        z = ZipCodeDatabase() 
        code = z[zipcode]

        city = weatherData['name']
        state = code.state

        #below: open the "city, state" locationLabel in google maps to see where it is 
        self.locationLabel.setText('<a href=https://www.google.com/maps/place/%s>(%s, %s)</a>' % (zipcode, city, state))
        self.locationLabel.setOpenExternalLinks(True)
        self.locationLabel.setToolTip("See %s, %s in Google Maps" % (city, state))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clockLabel.setText(_translate("MainWindow", "Showing Weather for:"))
        self.zipCodeLabel.setText(_translate("MainWindow", "Zip Code:"))
        self.tempLabel.setText(_translate("MainWindow", "--°"))
        self.conditionLabel.setText(_translate("MainWindow", ""))
        self.feelsLikeLabel.setText(_translate("MainWindow", "Feels Like:"))
        self.feelsLikeTemp.setText(_translate("MainWindow", "--°"))
        self.tempHiLabel.setText(_translate("MainWindow", "Hi:"))
        self.tempLoLabel.setText(_translate("MainWindow", "Lo:"))
        self.humidityLabel.setText(_translate("MainWindow", "Humidity:"))
        self.visibilityLabel.setText(_translate("MainWindow", "Visibility:"))
        self.sunriseLabel.setText(_translate("MainWindow", "Sunrise:"))
        self.sunsetLabel.setText(_translate("MainWindow", "Sunset:"))
        self.tempHiNum.setText(_translate("MainWindow", "--°"))
        self.tempLoNum.setText(_translate("MainWindow", "--°"))
        self.humidityNumLabel.setText(_translate("MainWindow", "--%"))
        self.visNumLabel.setText(_translate("MainWindow", "-- mi"))
        self.sunriseNumLabel.setText(_translate("MainWindow", "-:-- a"))
        self.sunsetNumLabel.setText(_translate("MainWindow", "-:-- p"))
        self.zipcodeLabel.setText(_translate("MainWindow", "-----"))
        self.locationLabel.setText(_translate("MainWindow", "(city, state)"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
