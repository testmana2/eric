# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Helpviewer/HelpTopicDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpTopicDialog(object):
    def setupUi(self, HelpTopicDialog):
        HelpTopicDialog.setObjectName("HelpTopicDialog")
        HelpTopicDialog.resize(500, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(HelpTopicDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(HelpTopicDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.topicsList = QtWidgets.QListWidget(HelpTopicDialog)
        self.topicsList.setObjectName("topicsList")
        self.verticalLayout.addWidget(self.topicsList)
        self.buttonBox = QtWidgets.QDialogButtonBox(HelpTopicDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.topicsList)

        self.retranslateUi(HelpTopicDialog)
        self.buttonBox.accepted.connect(HelpTopicDialog.accept)
        self.buttonBox.rejected.connect(HelpTopicDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HelpTopicDialog)
        HelpTopicDialog.setTabOrder(self.topicsList, self.buttonBox)

    def retranslateUi(self, HelpTopicDialog):
        _translate = QtCore.QCoreApplication.translate
        HelpTopicDialog.setWindowTitle(_translate("HelpTopicDialog", "Select Help Topic"))
        self.label.setText(_translate("HelpTopicDialog", "&Topics:"))
