# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MySQL(object):
    def setupUi(self, MySQL):
        MySQL.setObjectName("MySQL")
        MySQL.resize(473, 459)
        MySQL.setStyleSheet("background-color:white;")
        self.submit_PB = QtWidgets.QPushButton(MySQL)
        self.submit_PB.setGeometry(QtCore.QRect(190, 420, 93, 28))
        self.submit_PB.setStyleSheet("border:1px soild black;\n"
"border-radius:5px;\n"
"background-color:black;\n"
"color:white;\n"
"font-size:18px;")
        self.submit_PB.setObjectName("submit_PB")
        self.frame = QtWidgets.QFrame(MySQL)
        self.frame.setGeometry(QtCore.QRect(0, 0, 461, 141))
        self.frame.setStyleSheet("border:1px solid black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 72, 15))
        self.label_3.setStyleSheet("border-style:flat;")
        self.label_3.setObjectName("label_3")
        self.username_LE = QtWidgets.QLineEdit(self.frame)
        self.username_LE.setGeometry(QtCore.QRect(90, 40, 121, 21))
        self.username_LE.setObjectName("username_LE")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(260, 40, 41, 16))
        self.label.setStyleSheet("border-style:flat;")
        self.label.setObjectName("label")
        self.host_LE = QtWidgets.QLineEdit(self.frame)
        self.host_LE.setGeometry(QtCore.QRect(310, 40, 141, 21))
        self.host_LE.setObjectName("host_LE")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 72, 15))
        self.label_2.setStyleSheet("border-style:flat;")
        self.label_2.setObjectName("label_2")
        self.database_LE = QtWidgets.QLineEdit(self.frame)
        self.database_LE.setGeometry(QtCore.QRect(90, 90, 121, 21))
        self.database_LE.setObjectName("database_LE")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(230, 90, 72, 15))
        self.label_4.setStyleSheet("border-style:flat;")
        self.label_4.setObjectName("label_4")
        self.password_LE = QtWidgets.QLineEdit(self.frame)
        self.password_LE.setGeometry(QtCore.QRect(310, 90, 141, 21))
        self.password_LE.setObjectName("password_LE")
        self.frame_2 = QtWidgets.QFrame(MySQL)
        self.frame_2.setGeometry(QtCore.QRect(0, 150, 461, 261))
        self.frame_2.setStyleSheet("border:1px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.datetime_format_LE = QtWidgets.QLineEdit(self.frame_2)
        self.datetime_format_LE.setGeometry(QtCore.QRect(160, 190, 151, 21))
        self.datetime_format_LE.setObjectName("datetime_format_LE")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(20, 190, 121, 16))
        self.label_8.setStyleSheet("border-style:flat;")
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(80, 100, 61, 16))
        self.label_6.setStyleSheet("border-style:flat;")
        self.label_6.setObjectName("label_6")
        self.charset_LE = QtWidgets.QLineEdit(self.frame_2)
        self.charset_LE.setGeometry(QtCore.QRect(160, 100, 151, 21))
        self.charset_LE.setObjectName("charset_LE")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(80, 140, 61, 16))
        self.label_7.setStyleSheet("border-style:flat;")
        self.label_7.setObjectName("label_7")
        self.prefix_LE = QtWidgets.QLineEdit(self.frame_2)
        self.prefix_LE.setGeometry(QtCore.QRect(160, 150, 151, 21))
        self.prefix_LE.setObjectName("prefix_LE")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(90, 50, 51, 16))
        self.label_5.setStyleSheet("border-style:flat;")
        self.label_5.setObjectName("label_5")
        self.port_LE = QtWidgets.QLineEdit(self.frame_2)
        self.port_LE.setGeometry(QtCore.QRect(160, 50, 151, 21))
        self.port_LE.setObjectName("port_LE")
        self.label_9 = QtWidgets.QLabel(MySQL)
        self.label_9.setGeometry(QtCore.QRect(-9, 420, 121, 41))
        self.label_9.setStyleSheet("border:1px solid black;\n"
"font-size:20px;\n"
"")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(MySQL)
        self.submit_PB.clicked.connect(MySQL.submit)
        QtCore.QMetaObject.connectSlotsByName(MySQL)

    def retranslateUi(self, MySQL):
        _translate = QtCore.QCoreApplication.translate
        MySQL.setWindowTitle(_translate("MySQL", "MySQL配置"))
        self.submit_PB.setText(_translate("MySQL", "保存"))
        self.label_3.setText(_translate("MySQL", "username"))
        self.username_LE.setPlaceholderText(_translate("MySQL", "用户名"))
        self.label.setText(_translate("MySQL", "host"))
        self.host_LE.setPlaceholderText(_translate("MySQL", "服务器地址"))
        self.label_2.setText(_translate("MySQL", "database"))
        self.database_LE.setPlaceholderText(_translate("MySQL", "数据库名"))
        self.label_4.setText(_translate("MySQL", "password"))
        self.password_LE.setPlaceholderText(_translate("MySQL", "密码"))
        self.datetime_format_LE.setPlaceholderText(_translate("MySQL", "时间字段取出后的默认时间格式"))
        self.label_8.setText(_translate("MySQL", "datetime_format"))
        self.label_6.setText(_translate("MySQL", "charset"))
        self.charset_LE.setPlaceholderText(_translate("MySQL", "数据库编码（默认采用utf8）"))
        self.label_7.setText(_translate("MySQL", "prefix"))
        self.prefix_LE.setPlaceholderText(_translate("MySQL", "数据库表前缀"))
        self.label_5.setText(_translate("MySQL", "port"))
        self.port_LE.setPlaceholderText(_translate("MySQL", "端口"))
        self.label_9.setText(_translate("MySQL", "数据库配置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MySQL = QtWidgets.QWidget()
    ui = Ui_MySQL()
    ui.setupUi(MySQL)
    MySQL.show()
    sys.exit(app.exec_())
