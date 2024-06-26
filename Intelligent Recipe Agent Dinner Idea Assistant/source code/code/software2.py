from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommunityPage(object):
    def setupUi(self, CommunityPage):
        CommunityPage.setObjectName("CommunityPage")
        CommunityPage.resize(1107, 762)
        CommunityPage.setStyleSheet("*{\n"
"    border:none;\n"
"    background-color:white;\n"
"\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(CommunityPage)  # Modify this line to add the layout directly to CommunityPage
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(CommunityPage)
        self.header.setMinimumSize(QtCore.QSize(0, 70))
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.header)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:green")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.header)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"\n"
"    border-radius: 8px; /* 圆角的半径 */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(31, 140, 38); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 140, 38); \n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"\n"
"    border-radius: 8px; /* The radius of the rounded corners */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(31, 140, 38); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 140, 38); \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"\n"
"    border-radius: 8px; /* The radius of the rounded corners */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(31, 140, 38); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 140, 38); \n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.header)
        self.frame_3 = QtWidgets.QFrame(CommunityPage)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"     border-bottom: 2px solid rgb(214, 214, 214);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 0, 111, 51))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(31, 140, 38); /* Light green background */\n"
"    border: none;\n"
"    border-radius: 20px; /* filleted corner */\n"
"    color: white; /* White text */\n"
"    padding: 10px 20px; /* Padding */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 0, 71, 51))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: white; /* white background */\n"
"    border: 2px solid rgb(214, 214, 214); /* black frame */\n"
"    border-radius: 20px; /* filleted corner */\n"
"    color: black; /* Black text */\n"
"    padding: 10px 20px; /* Padding */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 14px;\n"
"\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 0, 101, 51))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(149, 149, 149); /* Grey background */\n"
"    border: none;\n"
"    border-radius: 20px; /* Grey background */\n"
"    color: white; /* Grey background */\n"
"    padding: 10px 20px; /* Padding */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setGeometry(QtCore.QRect(20, 20, 311, 331))
        self.frame_8.setStyleSheet("QFrame#frame_8{\n"
"     border-radius:15px;\n"
"     border: 2px solid rgb(214, 214, 214);\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setGeometry(QtCore.QRect(10, 10, 291, 181))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setGeometry(QtCore.QRect(10, 200, 291, 121))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        self.label_3.setGeometry(QtCore.QRect(3, 2, 271, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setGeometry(QtCore.QRect(0, 0, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        self.frame_14.setFont(font)
        self.frame_14.setStyleSheet("background-color:black\n"
"")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_4 = QtWidgets.QLabel(self.frame_12)
        self.label_4.setGeometry(QtCore.QRect(40, 0, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(31, 140, 38)")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_10)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_5 = QtWidgets.QLabel(self.frame_13)
        self.label_5.setGeometry(QtCore.QRect(3, 2, 271, 31))
        self.label_5.setStyleSheet("color:rgb(149, 149, 149)")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.frame_13)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(CommunityPage)
        QtCore.QMetaObject.connectSlotsByName(CommunityPage)

    def retranslateUi(self, CommunityPage):
        _translate = QtCore.QCoreApplication.translate
        CommunityPage.setWindowTitle(_translate("CommunityPage", "MainWindow"))
        self.label.setText(_translate("CommunityPage", "Eta Receipts"))
        self.pushButton.setText(_translate("CommunityPage", "Home"))
        self.pushButton_2.setText(_translate("CommunityPage", "Community"))
        self.pushButton_3.setText(_translate("CommunityPage", "Personal"))
        self.label_2.setText(_translate("CommunityPage", "Community"))
        self.pushButton_4.setText(_translate("CommunityPage", "Default"))
        self.pushButton_5.setText(_translate("CommunityPage", "A-Z"))
        self.pushButton_6.setText(_translate("CommunityPage", "Upload"))
        self.label_3.setText(_translate("CommunityPage", "Stir-Fried Beef with Broccoli"))
        self.label_4.setText(_translate("CommunityPage", "Lancelot"))
        self.label_5.setText(_translate("CommunityPage", "beef sirloin, broccoli florets, etc."))
