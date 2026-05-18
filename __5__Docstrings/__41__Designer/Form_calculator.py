# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(False)
        Form.resize(443, 374)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(48, 48))
        font = QFont()
        Form.setFont(font)
        Form.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Form.setStyleSheet(u"background-color: rgb(20, 20, 20);\n"
"color: rgb(220, 220, 220);\n"
"font-size: 18px;")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_15 = QPushButton(Form)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_15, 5, 2, 1, 1)

        self.pushButton_17 = QPushButton(Form)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_17, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"font-weight: bold;\n"
"background-color: #f31d58")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_4, 2, 2, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton.setCheckable(True)
        self.pushButton.setFlat(True)

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.pushButton_18 = QPushButton(Form)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setStyleSheet(u"font-weight: bold;\n"
"background-color: #f31d58")
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_18, 1, 3, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_5, 3, 2, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_6, 3, 1, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"font-weight: bold;\n"
"background-color: #f31d58")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_7, 3, 3, 1, 1)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_8, 3, 0, 1, 1)

        self.pushButton_11 = QPushButton(Form)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_11, 4, 2, 1, 1)

        self.pushButton_14 = QPushButton(Form)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_14, 4, 0, 1, 1)

        self.pushButton_12 = QPushButton(Form)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_12, 4, 3, 1, 1)

        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_10, 4, 1, 1, 1)

        self.pushButton_16 = QPushButton(Form)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"font-weight: bold;\n"
"background-color: #ff31be")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_16, 5, 3, 1, 1)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"                    border: none;\n"
"                    font-weight: bold;\n"
"                    background-color: #1e1e2d\n"
"                    }\n"
"                QPushButton:pressed {background-color: #bcaaa4}")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_9, 5, 0, 1, 2)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 54))
        self.lineEdit.setStyleSheet(u"border: none;\n"
"            border-bottom: 2px solid rgb(30, 30, 30);\n"
"            padding: 0 8px;\n"
"            font-size: 24px;\n"
"            font-weight: bold;")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("")
        self.pushButton_15.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"C", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"x", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

