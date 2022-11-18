# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commentScraping.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from storeScraping.scraping import trendyolScraping, hepsiburadaScraping
import time
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 440)
        MainWindow.setMinimumSize(QtCore.QSize(780, 440))
        MainWindow.setMaximumSize(QtCore.QSize(780, 440))
        MainWindow.setStyleSheet("background-color: rgb(29, 62, 83);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUrl.setGeometry(QtCore.QRect(50, 20, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.lineEditUrl.setFont(font)
        self.lineEditUrl.setStyleSheet("QLineEdit{\n"
"    color: rgb(255, 255, 255); \n"
"    border-radius: 10px;\n"
"    text-color: #FFFFF;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"    background-color: rgb(37, 75, 98);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(77, 84, 94);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(0, 173, 181);\n"
"    text-color: #FFFFF;\n"
"}")
        self.lineEditUrl.setText("")
        self.lineEditUrl.setFrame(True)
        self.lineEditUrl.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditUrl.setDragEnabled(False)
        self.lineEditUrl.setReadOnly(False)
        self.lineEditUrl.setClearButtonEnabled(True)
        self.lineEditUrl.setObjectName("lineEditUrl")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(330, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setToolTipDuration(-1)
        self.pushButtonStart.setAutoFillBackground(False)
        self.pushButtonStart.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    text-color: #FFFFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(71, 109, 124);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(0, 0, 0, 5);\n"
"}")
        self.pushButtonStart.setAutoDefault(False)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.textBrowserSomeData = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserSomeData.setGeometry(QtCore.QRect(20, 190, 451, 191))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.textBrowserSomeData.setFont(font)
        self.textBrowserSomeData.setStyleSheet("QTextBrowser{\n"
"    color: rgb(255, 255, 255); \n"
"    border-radius: 10px;\n"
"    text-color: #FFFFF;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"    background-color: rgb(37, 75, 98);\n"
"}")
        self.textBrowserSomeData.setObjectName("textBrowserSomeData")
        self.labelSomeData = QtWidgets.QLabel(self.centralwidget)
        self.labelSomeData.setGeometry(QtCore.QRect(30, 160, 441, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.labelSomeData.setFont(font)
        self.labelSomeData.setStyleSheet("color: rgb(255, 255, 255);\n"
"text-color: #FFFFF;\n"
"")
        self.labelSomeData.setScaledContents(False)
        self.labelSomeData.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSomeData.setWordWrap(False)
        self.labelSomeData.setObjectName("labelSomeData")
        self.pushButtonSaveCSV = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSaveCSV.setGeometry(QtCore.QRect(570, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButtonSaveCSV.setFont(font)
        self.pushButtonSaveCSV.setToolTipDuration(-1)
        self.pushButtonSaveCSV.setAutoFillBackground(False)
        self.pushButtonSaveCSV.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    text-color: #FFFFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(119, 171, 183);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(0, 0, 0, 5);\n"
"}")
        self.pushButtonSaveCSV.setAutoDefault(False)
        self.pushButtonSaveCSV.setObjectName("pushButtonSaveCSV")
        self.labelSave = QtWidgets.QLabel(self.centralwidget)
        self.labelSave.setGeometry(QtCore.QRect(490, 160, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.labelSave.setFont(font)
        self.labelSave.setStyleSheet("    color: rgb(255, 255, 255);\n"
"    text-color: #FFFFF;\n"
"")
        self.labelSave.setScaledContents(False)
        self.labelSave.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSave.setWordWrap(False)
        self.labelSave.setObjectName("labelSave")
        self.pushButtonSaveTXT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSaveTXT.setGeometry(QtCore.QRect(570, 270, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButtonSaveTXT.setFont(font)
        self.pushButtonSaveTXT.setToolTipDuration(-1)
        self.pushButtonSaveTXT.setAutoFillBackground(False)
        self.pushButtonSaveTXT.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    text-color: #FFFFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(119, 171, 183);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(0, 0, 0, 5);\n"
"}")
        self.pushButtonSaveTXT.setAutoDefault(False)
        self.pushButtonSaveTXT.setObjectName("pushButtonSaveTXT")
        self.pushButtonSaveEXCEL = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSaveEXCEL.setGeometry(QtCore.QRect(570, 340, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButtonSaveEXCEL.setFont(font)
        self.pushButtonSaveEXCEL.setToolTipDuration(-1)
        self.pushButtonSaveEXCEL.setAutoFillBackground(False)
        self.pushButtonSaveEXCEL.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    text-color: #FFFFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(119, 171, 183);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgba(0, 0, 0, 5);\n"
"}")
        self.pushButtonSaveEXCEL.setAutoDefault(False)
        self.pushButtonSaveEXCEL.setObjectName("pushButtonSaveEXCEL")
        self.labelInfoGithub = QtWidgets.QLabel(self.centralwidget)
        self.labelInfoGithub.setGeometry(QtCore.QRect(10, 400, 761, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.labelInfoGithub.setFont(font)
        self.labelInfoGithub.setStyleSheet("color: rgb(255, 255, 255);\n"
"text-color: #FFFFF;\n"
"")
        self.labelInfoGithub.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfoGithub.setObjectName("labelInfoGithub")
        self.labelOngoing = QtWidgets.QLabel(self.centralwidget)
        self.labelOngoing.setGeometry(QtCore.QRect(10, 122, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.labelOngoing.setFont(font)
        self.labelOngoing.setStyleSheet("color: rgb(255, 255, 255);\n"
"text-color: #FFFFF;\n"
"")
        self.labelOngoing.setScaledContents(False)
        self.labelOngoing.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOngoing.setWordWrap(False)
        self.labelOngoing.setObjectName("labelOngoing")
        self.textBrowserOngoing = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserOngoing.setGeometry(QtCore.QRect(180, 120, 581, 28))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.textBrowserOngoing.setFont(font)
        self.textBrowserOngoing.setStyleSheet("QTextBrowser{\n"
"    color: rgba(255, 85, 0, 120); \n"
"    border-radius: 10px;\n"
"    text-color: rgba(255, 85, 0, 254);\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"    background-color: rgb(37, 75, 98);\n"
"}")
        self.textBrowserOngoing.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserOngoing.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserOngoing.setReadOnly(True)
        self.textBrowserOngoing.setTabStopWidth(1)
        self.textBrowserOngoing.setObjectName("textBrowserOngoing")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        try:
            self.pushButtonStart.clicked.connect(self.readURL)
        except:
            self.processInfo("Something went wrong")

    def message(self, mType, message, buttonStatus = QtWidgets.QMessageBox.Ok):
        messageBox = QtWidgets.QMessageBox()
        # <------ Information / Warning / Question / Critical ------>
        if mType == "Information":
            messageBox.setIcon(QtWidgets.QMessageBox.Information)
        elif mType == "Warning":
            messageBox.setIcon(QtWidgets.QMessageBox.Warning)
        elif mType == "Question":
            messageBox.setIcon(QtWidgets.QMessageBox.Question)
        elif mType == "Critical":
            messageBox.setIcon(QtWidgets.QMessageBox.Critical)

        messageBox.setText(message)
        messageBox.setWindowTitle(mType)
        messageBox.setStandardButtons(buttonStatus)
        retval = messageBox.exec_()

    def readURL(self):
        lastTime = time.time()
        if self.lineEditUrl.text() == "":
            self.message("Warning", "Please enter a link")

        else:
            url = self.lineEditUrl.text().split("/")[2]
            if url == "www.trendyol.com":
                timeIsUp = self.timer(lastTime, 3)
                print(lastTime)
                if timeIsUp == True:
                    df = trendyolScraping(str(self.lineEditUrl.text()))
                    writeDf = """
                    {}
                    """.format(df.head())
                    self.processInfo("Extracting data from Trendyol has been successfully completed.")
                    self.textBrowserSomeData.setText(writeDf.lstrip())
            elif url == "www.hepsiburada.com":
                timeIsUp = self.timer(lastTime, 3)
                if timeIsUp == True:
                    df = hepsiburadaScraping(self.lineEditUrl.text())
                    writeDf = """
                    {}
                    """.format(df.head())
                    self.processInfo("Extracting data from Hepsiburada has been successfully completed.")
                    self.textBrowserSomeData.setText(writeDf.lstrip())

            elif url == "www.n11.com":
                self.processInfo("Systems are being prepared to extract data from N11.")

            else:
                self.message("Critical",
                             "The link you entered is out of the workspace!\nPlease try to scrape data only for Trendyol, Hepsiburada and N11.\nYour link: {}".format(url))

    def processInfo(self,process):
        self.textBrowserOngoing.clear()
        self.textBrowserOngoing.setText(process)

    def timer(self, lastTime, delay):
        while True:
            if time.time() - lastTime < delay: continue
            elif time.time() - lastTime > delay:
                timeIsUp = True
                return timeIsUp

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CommentScraping github.com/ismaildrcn"))
        self.lineEditUrl.setPlaceholderText(_translate("MainWindow", "URL"))
        self.pushButtonStart.setText(_translate("MainWindow", "Start"))
        self.labelSomeData.setText(_translate("MainWindow", "Some Data"))
        self.pushButtonSaveCSV.setText(_translate("MainWindow", "CSV"))
        self.labelSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonSaveTXT.setText(_translate("MainWindow", "TXT"))
        self.pushButtonSaveEXCEL.setText(_translate("MainWindow", "EXCEL"))
        self.labelInfoGithub.setText(_translate("MainWindow", "Comment Scraping github.com/ismaildrcn"))
        self.labelOngoing.setText(_translate("MainWindow", "Ongoing transactions"))
        self.textBrowserOngoing.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tahoma\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
