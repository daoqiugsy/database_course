# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manager.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Mbox(object):
    def setupUi(self, Mbox):
        Mbox.setObjectName("Mbox")
        Mbox.resize(265, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../收藏夹/iCloud Photos/Downloads/2019/IMG_0574.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Mbox.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Mbox)
        self.label.setGeometry(QtCore.QRect(5, 51, 61, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Mbox)
        self.label_2.setGeometry(QtCore.QRect(5, 87, 61, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Mbox)
        self.label_4.setGeometry(QtCore.QRect(5, 159, 61, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.nanButton = QtWidgets.QRadioButton(Mbox)
        self.nanButton.setGeometry(QtCore.QRect(90, 120, 41, 19))
        self.nanButton.setObjectName("nanButton")
        self.MnoEdit = QtWidgets.QLineEdit(Mbox)
        self.MnoEdit.setGeometry(QtCore.QRect(75, 51, 146, 21))
        self.MnoEdit.setReadOnly(False)
        self.MnoEdit.setClearButtonEnabled(True)
        self.MnoEdit.setObjectName("MnoEdit")
        self.okButton = QtWidgets.QPushButton(Mbox)
        self.okButton.setGeometry(QtCore.QRect(60, 240, 71, 28))
        self.okButton.setObjectName("okButton")
        self.label_5 = QtWidgets.QLabel(Mbox)
        self.label_5.setGeometry(QtCore.QRect(5, 195, 60, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.MnameEdit = QtWidgets.QLineEdit(Mbox)
        self.MnameEdit.setGeometry(QtCore.QRect(75, 87, 146, 21))
        self.MnameEdit.setClearButtonEnabled(True)
        self.MnameEdit.setObjectName("MnameEdit")
        self.nvButton = QtWidgets.QRadioButton(Mbox)
        self.nvButton.setGeometry(QtCore.QRect(160, 120, 41, 19))
        self.nvButton.setObjectName("nvButton")
        self.MphonEdit = QtWidgets.QLineEdit(Mbox)
        self.MphonEdit.setGeometry(QtCore.QRect(75, 195, 146, 21))
        self.MphonEdit.setClearButtonEnabled(True)
        self.MphonEdit.setObjectName("MphonEdit")
        self.cancelButton = QtWidgets.QPushButton(Mbox)
        self.cancelButton.setGeometry(QtCore.QRect(150, 240, 71, 28))
        self.cancelButton.setObjectName("cancelButton")
        self.label_3 = QtWidgets.QLabel(Mbox)
        self.label_3.setGeometry(QtCore.QRect(5, 123, 61, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.MageEdit = QtWidgets.QLineEdit(Mbox)
        self.MageEdit.setGeometry(QtCore.QRect(75, 159, 146, 21))
        self.MageEdit.setClearButtonEnabled(True)
        self.MageEdit.setObjectName("MageEdit")
        self.msg = QtWidgets.QLabel(Mbox)
        self.msg.setGeometry(QtCore.QRect(30, 10, 201, 16))
        self.msg.setObjectName("msg")

        self.retranslateUi(Mbox)
        QtCore.QMetaObject.connectSlotsByName(Mbox)

    def retranslateUi(self, Mbox):
        _translate = QtCore.QCoreApplication.translate
        Mbox.setWindowTitle(_translate("Mbox", "工作人员信息盒"))
        self.label.setText(_translate("Mbox", "工号"))
        self.label_2.setText(_translate("Mbox", "姓名"))
        self.label_4.setText(_translate("Mbox", "年龄"))
        self.nanButton.setText(_translate("Mbox", "男"))
        self.okButton.setText(_translate("Mbox", "确定"))
        self.label_5.setText(_translate("Mbox", "联系方式"))
        self.nvButton.setText(_translate("Mbox", "女"))
        self.cancelButton.setText(_translate("Mbox", "取消"))
        self.label_3.setText(_translate("Mbox", "性别"))
        self.msg.setText(_translate("Mbox", "提示信息"))

