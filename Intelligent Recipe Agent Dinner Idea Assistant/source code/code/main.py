import sys
import openai
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget

from software import Ui_HomePage
from software2 import Ui_CommunityPage
from software3 import Ui_PersonalPage
import respond

class MyMainForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)  # Set window flag: Hide window border
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(1107, 758)  # Set the initial window size
        self.evn = 0

        # Set UI
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.stackedWidget)

        # Initialize three pages
        self.homePage = QtWidgets.QWidget()
        self.communityPage = QtWidgets.QWidget()
        self.personalPage = QtWidgets.QWidget()

        # Set up the UI for three pages
        self.home_ui = Ui_HomePage()
        self.home_ui.setupUi(self.homePage)

        self.community_ui = Ui_CommunityPage()
        self.community_ui.setupUi(self.communityPage)

        self.personal_ui = Ui_PersonalPage()
        self.personal_ui.setupUi(self.personalPage)

        # Add the page to stackedWidget
        self.stackedWidget.addWidget(self.homePage)
        self.stackedWidget.addWidget(self.communityPage)
        self.stackedWidget.addWidget(self.personalPage)

        # Set button connection
        self.home_ui.pushButton.clicked.connect(self.show_home)
        self.home_ui.pushButton_2.clicked.connect(self.show_community)
        self.home_ui.pushButton_3.clicked.connect(self.show_personal)

        self.community_ui.pushButton.clicked.connect(self.show_home)
        self.community_ui.pushButton_2.clicked.connect(self.show_community)
        self.community_ui.pushButton_3.clicked.connect(self.show_personal)

        self.personal_ui.pushButton.clicked.connect(self.show_home)
        self.personal_ui.pushButton_2.clicked.connect(self.show_community)
        self.personal_ui.pushButton_3.clicked.connect(self.show_personal)

    def show_home(self):
        self.stackedWidget.setCurrentWidget(self.homePage)

    def show_community(self):
        self.stackedWidget.setCurrentWidget(self.communityPage)

    def show_personal(self):
        self.stackedWidget.setCurrentWidget(self.personalPage)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
