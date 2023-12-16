from PyQt5 import QtCore, QtGui, QtWidgets
WIDTH=200
HEIGHT=200

class Ui_Selecting_Client(object):
    def setupUi(self, Selecting_Client:QtWidgets.QMainWindow):
        Selecting_Client.setObjectName("Selecting_Client")
        Selecting_Client.resize(WIDTH, HEIGHT)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Selecting_Client.sizePolicy().hasHeightForWidth())
        Selecting_Client.setSizePolicy(sizePolicy)
        Selecting_Client.setMinimumSize(QtCore.QSize(WIDTH, HEIGHT))
        Selecting_Client.setMaximumSize(QtCore.QSize(WIDTH, HEIGHT))
        Selecting_Client.setAcceptDrops(False)
        self.Discription = QtWidgets.QLabel(Selecting_Client)
        self.Discription.setGeometry(QtCore.QRect(10, 10, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.Discription.setFont(font)
        self.Discription.setObjectName("Discription")
        self.retranslateUi_init(Selecting_Client)
        QtCore.QMetaObject.connectSlotsByName(Selecting_Client)
        self.Selecting_Client=Selecting_Client
        self.nextbuttontop=70
    
    def MainWindowsetup(self,MainWindow:QtWidgets.QStackedWidget):
        MainWindow.resize(WIDTH, HEIGHT)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(WIDTH, HEIGHT))
        MainWindow.setMaximumSize(QtCore.QSize(WIDTH, HEIGHT))
        MainWindow.setAcceptDrops(False)

    def addbutton(self,text:str) -> QtWidgets.QPushButton:
        pushButton = QtWidgets.QPushButton(self.Selecting_Client)
        pushButton.setGeometry(QtCore.QRect(40, self.nextbuttontop, 111, 31))
        self.nextbuttontop+=41
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(12)
        pushButton.setFont(font)
        pushButton.setObjectName(text)
        _translate = QtCore.QCoreApplication.translate
        pushButton.setText(_translate("Selecting_Client",text))
        return pushButton

    def retranslateUi_init(self, Selecting_Client:QtWidgets.QWidget):
        _translate = QtCore.QCoreApplication.translate
        Selecting_Client.setWindowTitle(_translate("Selecting_Client", "Youtube Title Displayer"))
        self.Discription.setText(_translate("Selecting_Client", "請選擇要偵測的視窗"))