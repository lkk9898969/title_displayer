import win32gui
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import pygetwindow as gw
mutex=QtCore.QMutex()
waiting=QtCore.QWaitCondition()
detect_text="YouTube標題"
import icon
WIDTH=482
HEIGHT=45
# --------------UI--------------- #
class Ui_detecting(object):
    def setupUi(self, Detecting_Client:QtWidgets.QWidget):
        Detecting_Client.setObjectName("Detecting_Client")
        Detecting_Client.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Detecting_Client.sizePolicy().hasHeightForWidth())
        Detecting_Client.setSizePolicy(sizePolicy)
        Detecting_Client.setMinimumSize(QtCore.QSize(200, 90))
        Detecting_Client.setMaximumSize(QtCore.QSize(200, 90))
        self.text = QtWidgets.QLabel(Detecting_Client)
        self.text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.text.setGeometry(QtCore.QRect(10, 25, 180, 40))
        font = QtGui.QFont()
        font.setFamily("AdLib WGL4 BT")
        font.setPointSize(15)
        self.text.setFont(font)
        self.text.setObjectName("text")
        Detecting_Client.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)

        self.retranslateUi(Detecting_Client)
        QtCore.QMetaObject.connectSlotsByName(Detecting_Client)

    def retranslateUi(self, Detecting_Client:QtWidgets.QWidget):
        _translate = QtCore.QCoreApplication.translate
        Detecting_Client.setWindowTitle(_translate("dectecting", "Youtube Title Displayer"))
        self.text.setText(_translate("Detecting_Client", "偵測{}中...").format(detect_text))

class Ui_MainWindow(object):
    def setupUi(self, music_display:QtWidgets.QWidget):
        music_display.setObjectName("music_display")
        music_display.resize(WIDTH, HEIGHT)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(music_display.sizePolicy().hasHeightForWidth())
        music_display.setSizePolicy(sizePolicy)
        music_display.setMinimumSize(QtCore.QSize(WIDTH, HEIGHT))
        music_display.setMaximumSize(QtCore.QSize(WIDTH, HEIGHT))
        if True:
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
            music_display.setPalette(palette)
        music_display.setAcceptDrops(False)
        self.music_name = QtWidgets.QLabel(music_display)
        self.music_name.setGeometry(QtCore.QRect(0, 0, 481, 41))
        self.font = QtGui.QFont()
        self.font.setFamily("微軟正黑體")
        self.font.setPointSize(16)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.qfmetrics=QtGui.QFontMetrics(self.font)
        self.music_name.setFont(self.font)
        self.music_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.music_name.setObjectName("music_name")
        music_display.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)

        self.retranslateUi(music_display)
        QtCore.QMetaObject.connectSlotsByName(music_display)
        # shell.SendKeys('%')

    def retranslateUi(self, music_display):
        _translate = QtCore.QCoreApplication.translate
        music_display.setWindowTitle(_translate("music_display", "Youtube Title Displayer"))
        self.music_name.setText(_translate("music_display", ""))
    
        


# --------------UI--------------- #

# --------------Controller--------------- #
# shell = win32com.client.Dispatch("WScript.Shell")
class detecting_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_detecting()
        self.ui.setupUi(self)
        self.setup_control()
    
    def setup_control(self):
        self.setWindowIcon(i)
        global yt
        self.qdecting=detecting()
        self.qdecting.qisgnal.connect(self.decting)
        self.qdecting.start()

    def decting(self):
        self.close()
        self.w = MainWindow_controller()
        self.w.showMinimized()
        self.w.show()
        self.w.showMaximized()
        self.w.showNormal()
        qr = self.w.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.w.move(qr.topLeft())
        

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.dplength=20
        self.setWindowIcon(i)
        self.string = win32gui.GetWindowText(yt)
        self.qt_movefunction = QtCore.QThread()
        self.qt_movefunction.run = self.movefunction
        self.qt_movefunction.start()
        self.checkfuntion = checkfunction()
        self.checkfuntion.qsignal.connect(self.changestr)
        self.checkfuntion.start()

    def changestr(self,value):
        self.movestartstate = False
        self.string = title_process(value)
        self.qt_movefunction.quit()
        self.qt_movefunction.wait()
        while(self.qt_movefunction.isRunning()):
            pass
        self.qt_movefunction = QtCore.QThread()
        self.qt_movefunction.run = self.movefunction
        self.qt_movefunction.start()
        waiting.wakeAll()

    def movefunction(self):
        self.string=title_process(self.string)
        self.ui.music_name.setText(self.string)
        self.movestartstate = True
        self.dpiwidth=self.dpi_pos(self.string)
        if (self.dpiwidth < WIDTH):
            self.movestartstate = False
            self.ui.music_name.setGeometry(0,0,self.dpiwidth,HEIGHT)
        while(self.movestartstate):
            self.ui.music_name.setGeometry(0,0,self.dpiwidth,HEIGHT)
            sleep(1)
            for i in range(self.dpiwidth-WIDTH):
                if not (self.movestartstate):
                    break
                sleep(0.03)
                try:
                    self.ui.music_name.move(-i,0)
                except RuntimeError:
                    self.movestartstate=False
                    break
            sleep(1)
    
    def dpi_pos(self,text:str):
        return self.ui.qfmetrics.width(text)



# --------------Controller--------------- #
# --------------QThread--------------- #
def title_process(title:str):
    titlepos=title.find(" - YouTube")
    if titlepos != -1:
        title=title[:titlepos]
    return title

class detecting(QtCore.QThread):
    qisgnal=QtCore.pyqtSignal(int)
    def run(self):
        global yt
        yt=0
        for i in gw.getAllTitles():
            if ' - Microsoft​ Edge' in i:
                if ' - YouTube' in i:
                    yt = win32gui.FindWindowEx(None,None,None, i)
        sleep(1)
        while (yt == 0):
            sleep(1)
            for i in gw.getAllTitles():
                if ' - Microsoft​ Edge' in i:
                    if ' - YouTube' in i:
                        yt = win32gui.FindWindowEx(None,None,None, i)
        self.qisgnal.emit(yt)

class checkfunction(QtCore.QThread):
    qsignal = QtCore.pyqtSignal(str)
    checkstartstate = True
    def run(self):
        yt_title = win32gui.GetWindowText(yt)
        while(self.checkstartstate):
            yt_title_new = win32gui.GetWindowText(yt)
            if (yt_title_new != yt_title):
                mutex.lock()
                yt_title=yt_title_new
                self.qsignal.emit(yt_title)
                waiting.wait(mutex)
                mutex.unlock()

# --------------QThread--------------- #

# --------------Start--------------- #

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pm = QtGui.QPixmap()
    pm.loadFromData(icon.b64decode(icon.img))
    i = QtGui.QIcon()
    i.addPixmap(pm)
    window = detecting_controller()
    window.show()
    sys.exit(app.exec_())
    
# --------------Start--------------- #