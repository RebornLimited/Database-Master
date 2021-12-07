from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pymysql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 522)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Download/4417104_database_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 601, 571))
        self.tabs.setStyleSheet("background-color: rgb(62, 62, 62);\n"
"color: rgb(255, 255, 255);")
        self.tabs.setObjectName("tabs")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setStyleSheet("")
        self.tab_1.setObjectName("tab_1")
        self.label_title = QtWidgets.QLabel(self.tab_1)
        self.label_title.setGeometry(QtCore.QRect(100, 0, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_title.setObjectName("label_title")
        self.lineEdit_host = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_host.setGeometry(QtCore.QRect(0, 180, 111, 31))
        self.lineEdit_host.setStyleSheet("color: rgb(170, 170, 170);")
        self.lineEdit_host.setText("")
        self.lineEdit_host.setPlaceholderText("")
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.label_host = QtWidgets.QLabel(self.tab_1)
        self.label_host.setGeometry(QtCore.QRect(0, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_host.setFont(font)
        self.label_host.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_host.setObjectName("label_host")
        self.label_user = QtWidgets.QLabel(self.tab_1)
        self.label_user.setGeometry(QtCore.QRect(120, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_user.setFont(font)
        self.label_user.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_user.setObjectName("label_user")
        self.lineEdit_user = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_user.setGeometry(QtCore.QRect(110, 180, 121, 31))
        self.lineEdit_user.setStyleSheet("color: rgb(170, 170, 170);")
        self.lineEdit_user.setText("")
        self.lineEdit_user.setPlaceholderText("")
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.label_password = QtWidgets.QLabel(self.tab_1)
        self.label_password.setGeometry(QtCore.QRect(240, 130, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_password.setObjectName("label_password")
        self.lineEdit_password = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_password.setGeometry(QtCore.QRect(230, 180, 141, 31))
        self.lineEdit_password.setStyleSheet("color: rgb(170, 170, 170);")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setPlaceholderText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_database = QtWidgets.QLabel(self.tab_1)
        self.label_database.setGeometry(QtCore.QRect(380, 130, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_database.setFont(font)
        self.label_database.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_database.setObjectName("label_database")
        self.lineEdit_database = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_database.setGeometry(QtCore.QRect(370, 180, 141, 31))
        self.lineEdit_database.setStyleSheet("color: rgb(170, 170, 170);")
        self.lineEdit_database.setText("")
        self.lineEdit_database.setPlaceholderText("")
        self.lineEdit_database.setObjectName("lineEdit_database")
        self.label_request = QtWidgets.QLabel(self.tab_1)
        self.label_request.setGeometry(QtCore.QRect(200, 300, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_request.setFont(font)
        self.label_request.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_request.setObjectName("label_request")
        self.lineEdit_request = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_request.setGeometry(QtCore.QRect(0, 360, 511, 51))
        self.lineEdit_request.setStyleSheet("color: rgb(170, 170, 170);")
        self.lineEdit_request.setText("")
        self.lineEdit_request.setPlaceholderText("")
        self.lineEdit_request.setObjectName("lineEdit_request")
        self.btn_done = QtWidgets.QPushButton(self.tab_1)
        self.btn_done.setGeometry(QtCore.QRect(190, 420, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_done.setFont(font)
        self.btn_done.setStyleSheet("background-color: rgb(222, 148, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_done.setObjectName("btn_done")
        self.sorry_text = QtWidgets.QLabel(self.tab_1)
        self.sorry_text.setGeometry(QtCore.QRect(120, 0, 400, 16))
        self.sorry_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.sorry_text.setObjectName("sorry_text")
        self.lineEdit_port = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_port.setGeometry(QtCore.QRect(200, 260, 111, 31))
        self.lineEdit_port.setStyleSheet("color: rgb(170, 170, 170);")
        self.lineEdit_port.setText("")
        self.lineEdit_port.setPlaceholderText("")
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.label_port = QtWidgets.QLabel(self.tab_1)
        self.label_port.setGeometry(QtCore.QRect(200, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_port.setFont(font)
        self.label_port.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_port.setObjectName("label_port")
        self.tabs.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_version = QtWidgets.QLabel(self.tab_2)
        self.label_version.setGeometry(QtCore.QRect(10, -10, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_version.setObjectName("label_version")
        self.label_updates = QtWidgets.QLabel(self.tab_2)
        self.label_updates.setGeometry(QtCore.QRect(10, 40, 241, 31))
        self.label_updates.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_updates.setObjectName("label_updates")
        self.tabs.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.done()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Database Master"))
        self.label_title.setText(_translate("MainWindow", "DATABASE MASTER"))
        self.label_host.setText(_translate("MainWindow", "Host"))
        self.label_user.setText(_translate("MainWindow", "User"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.label_database.setText(_translate("MainWindow", "Database"))
        self.label_request.setText(_translate("MainWindow", "Request"))
        self.btn_done.setText(_translate("MainWindow", "Done"))
        self.sorry_text.setText(_translate("MainWindow", "I sincerely apologize for this design. It will be improved in the future."))
        self.label_port.setText(_translate("MainWindow", "Port"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_1), _translate("MainWindow", "Menu"))
        self.label_version.setText(_translate("MainWindow", "Version: 1.0.0"))
        self.label_updates.setText(_translate("MainWindow", "There will definitely be something here..."))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("MainWindow", "Updates"))

    def done(self):
        self.btn_done.clicked.connect(self.main)

    def main(self):
        try:
            connection = pymysql.connect(
                host=self.lineEdit_host.text(),
                port=int(self.lineEdit_port.text()),
                user=self.lineEdit_user.text(),
                password=self.lineEdit_password.text(),
                database=self.lineEdit_database.text(),
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected!")

            try:
                with connection.cursor() as cursor:
                    request = f"{self.lineEdit_request.text()}"
                    cursor.execute(request)
                    connection.commit()
                    print("Operation completed successfully!")
            finally:
                connection.close()
        except Exception as ex:
            print("Connection failed...")
            print(ex)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
