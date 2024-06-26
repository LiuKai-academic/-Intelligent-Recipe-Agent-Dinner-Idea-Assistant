from PyQt5 import QtCore, QtGui, QtWidgets
import time
import openai
from respond import respond
from sd import generate_image


class Ui_HomePage(object):
    def setupUi(self, HomePage):
        self.conversation_history = [
            "From now on, you're gonna be my smart kitchen butler. You need to act more naturally, as if you were chatting with me again. Here is a transcript of our chat, and you need to respond to the unanswered questions at the bottom."]

        HomePage.setObjectName("HomePage")
        HomePage.resize(1107, 758)
        HomePage.setStyleSheet("*{\n"
                               "    border:none;\n"
                               "    background-color:white;\n"
                               "\n"
                               "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(HomePage)  # Add the layout directly to a HomePage
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(HomePage)
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
        self.frame_3 = QtWidgets.QFrame(HomePage)
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(31)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QPushButton {\n"
                                   "    border-radius: 8px; /* Set the radius of the rounded corners */\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: red; /* The border turns red when the mouse hovers */\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setEnabled(True)
        self.frame_6.setMaximumSize(QtCore.QSize(375, 16777215))
        self.frame_6.setStyleSheet("\n"
                                   ".QFrame#frame_6{\n"
                                   "    border-style: solid; /* The border style is solid */\n"
                                   "    border-width: 2px; /* The border width is 1 pixel */\n"
                                   "    border-color: rgb(214, 214, 214); /* The border color is gray */\n"
                                   "    border-radius: 50px;\n"
                                   "    background-color: #FAFAF5;\n"
                                   "}\n"
                                   "")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4.addWidget(self.frame_8)
        self.chatBox = QtWidgets.QTextEdit(self.frame_8)  # Add the chat history display box to frame 8
        self.chatBox.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.chatBox.setReadOnly(True)
        self.verticalLayout_4.addWidget(self.chatBox)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setStyleSheet("QFrame#frame_7 {\n"
                                   "    border-style: solid; /* The border style is solid */\n"
                                   "    border-width: 2px; /* The border width is 1 pixel */\n"
                                   "    border-color: rgb(214, 214, 214); /* The border color is gray */\n"
                                   "    border-radius: 50px;\n"
                                   "    background-color: #FAFAF5;\n"
                                   "}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_12 = QtWidgets.QFrame(self.frame_7)
        self.frame_12.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_6.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_12)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_6.addWidget(self.frame_15)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_7)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_13.setStyleSheet("QFrame {\n"
                                    "    background-color: rgba(0, 0, 0, 0); /* completely transparent */\n"
                                    "}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 271, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 10, 71, 30))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 8px;\n"
                                        "    background-color: rgb(31, 140, 38); \n"
                                        "    color: white;\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.handle_input)  # Connect button click event
        self.verticalLayout_5.addWidget(self.frame_13)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_3)

        self.recipeLabel = QtWidgets.QLabel(self.frame_14)  # Add a recipe display box
        self.recipeLabel.setWordWrap(True)
        self.recipeLabel.setGeometry(QtCore.QRect(0, 0, 250, 400))
        self.recipeLabel.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.recipeImage = QtWidgets.QLabel(self.frame_15)  # Add recipe picture display box
        self.recipeImage.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.recipeImage.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        _translate = QtCore.QCoreApplication.translate
        HomePage.setWindowTitle(_translate("HomePage", "MainWindow"))
        self.label.setText(_translate("HomePage", "Eta Recipe"))
        self.pushButton.setText(_translate("HomePage", "Home"))
        self.pushButton_2.setText(_translate("HomePage", "Community"))
        self.pushButton_3.setText(_translate("HomePage", "Personal"))
        self.label_2.setText(_translate("HomePage", "What to eat today..."))
        self.pushButton_4.setText(_translate("HomePage", "Send"))

    def handle_input(self):
        user_input = self.lineEdit.text()
        if user_input:
            if "show me the recipe" in user_input:
                response_text = respond(self.conversation_history, user_input)
                self.chatBox.append("User: " + user_input)
                self.chatBox.append("Assistance: Sure, the recipe is on your right.")
                self.recipeLabel.setText(response_text)
                self.conversation_history.append(response_text)
                pixmap = QtGui.QPixmap(generate_image(response_text))
                self.recipeImage.setPixmap(pixmap)
                self.lineEdit.clear()

            else:
                response_text = respond(self.conversation_history, user_input)
                self.chatBox.append("User: " + user_input)
                self.chatBox.append(response_text)
                self.conversation_history.append(response_text)
                self.lineEdit.clear()


