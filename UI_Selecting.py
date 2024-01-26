from PyQt5 import QtCore, QtGui, QtWidgets
WIDTH=200
HEIGHT=200

class Ui_Selecting_Client(object):
    def __setupUI(self,Widget:QtWidgets.QWidget):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.resize(WIDTH, HEIGHT)
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QtCore.QSize(WIDTH, HEIGHT))
        Widget.setMaximumSize(QtCore.QSize(WIDTH, HEIGHT))
        Widget.setAcceptDrops(False)

    def setupUi(self, Selecting_Client:QtWidgets.QMainWindow):
        Selecting_Client.setObjectName("Selecting_Client")
        self.__setupUI(Selecting_Client)
        self.__setupUI(Selecting_Client.parent())
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

    def uiaddbutton(self,text:str) -> QtWidgets.QPushButton:
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