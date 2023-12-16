import typing
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget
import win32gui
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import pygetwindow as gw
import UI
from detectelement import element as detectelement

import icon

# --------------Controller--------------- #
# shell = win32com.client.Dispatch("WScript.Shell")
# ------------Main Controller------------ #
class MainWindow_controller(QtWidgets.QStackedWidget):
    def __init__(self,icon:QtGui.QIcon) -> None:
        super().__init__()
        self.setupUI(icon)
        self.switch_to_selecting()

    def setupUI(self,icon:QtGui.QIcon):
        self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.setWindowTitle("Youtube Title Displayer")
        self.setWindowIcon(icon)

    def switch_to_selecting(self):
        self.selecting=selecting_controller(self)
        self.selecting_button_init()
        index=self.addWidget(self.selecting)
        self.setCurrentIndex(index)
    
    def selecting_button_init(self):
        '''
        initial the button and element.
        Note that the first element.windowtitle will be the cutoff point for the title to display.
        '''
        for i in self.datainit():
            self.addbutton(i)

    def datainit(self) -> list[detectelement]:
        _result=[]
        i=detectelement("Youtube"," - YouTube"," - Microsoft​ Edge")
        _result.append(i)
        i=detectelement("VLC"," - VLC")
        _result.append(i)
        return _result

    def addbutton(self,element:detectelement):
        button=self.selecting.addbutton(element.text)
        button.clicked.connect(lambda state,element=element:self.switch_to_detecting(element))

    def switch_to_detecting(self,element:detectelement):
        self.dectecting=detecting_controller(self,element,lambda hwnd,filters=element.windowtitle:self.display(hwnd,filters))
        index=self.addWidget(self.dectecting)
        self.setCurrentIndex(index)

    def display(self,hwnd,filters:tuple[str]):
        self.displaying = DisplayWindow_controller(self,hwnd,filters)
        index=self.addWidget(self.displaying)
        self.setCurrentIndex(index)
        self.showMinimized()
        self.show()
        self.showMaximized()
        self.showNormal()
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# ----------Selecting Controller--------- #
class selecting_controller(QtWidgets.QWidget):
    def __init__(self,MainWindow) -> None:
        super().__init__(MainWindow)
        self.ui = UI.Ui_Selecting_Client()
        self.ui.setupUi(self)
        self.ui.MainWindowsetup(MainWindow)

    def addbutton(self,text:str):
        return self.ui.addbutton(text)

# ----------Detecting Controller--------- #
class detecting_controller(QtWidgets.QWidget):
    detectingsignal=QtCore.pyqtSignal(int)
    def __init__(self,MainWindow,element:detectelement,func):
        '''
        func : the fuction that detectingsignal connect.
        detectingsignal will emit a hwnd.
        '''
        super().__init__(MainWindow) # in python3, super(Class, self).xxx = super().xxx
        self.ui = UI.Ui_Detecting()
        self.ui.setupUi(self,element.text)
        self.ui.MainWindowsetup(MainWindow)
        self.setup_control(element,func)
    
    def setup_control(self,element:detectelement,func):
        self.setWindowIcon(i)
        self.detectingsignal.connect(func)
        self.element=element
        self.qdecting=self.detecting(self,element=self.element)
        self.qdecting.qisgnal.connect(lambda signal:self.detectingsignal.emit(signal))
        self.qdecting.start()
    
    class detecting(QtCore.QThread):
        qisgnal=QtCore.pyqtSignal(int)
        def __init__(self, parent: QObject | None = ...,element:detectelement = ...) -> None:
            super().__init__(parent)
            self.element=element
        def run(self):
            yt=0
            for i in gw.getAllTitles():
                flag=True
                for j in self.element.windowtitle:
                    if j in i:
                        continue
                    else:
                        flag=False
                        break
                if not flag:
                    continue
                yt = win32gui.FindWindowEx(None,None,None, i)
                break
            sleep(1)
            while (yt == 0):
                sleep(1)
                for i in gw.getAllTitles():
                    flag=True
                    for j in self.element.windowtitle:
                        if j in i:
                            continue
                        else:
                            flag=False
                            break
                    if not flag:
                        continue
                    yt = win32gui.FindWindowEx(None,None,None, i)
                    break
            self.qisgnal.emit(yt)

# ---------DisplayWindow Controller--------- #
class DisplayWindow_controller(QtWidgets.QWidget):
    def __init__(self,MainWindow,hwnd,filters):
        super().__init__(MainWindow) # in python3, super(Class, self).xxx = super().xxx
        self.ui = UI.Ui_display_music_name()
        self.ui.setupUi(self)
        self.ui.MainWindowsetup(MainWindow)
        self.setup_control(hwnd,filters)

    def setup_control(self,hwnd,filters):
        self.mutex=QtCore.QMutex()
        self.waiting=QtCore.QWaitCondition()
        self.dplength=20
        self.setWindowIcon(i)
        self.filters=filters
        self.string = win32gui.GetWindowText(hwnd)
        self.qt_movefunction = QtCore.QThread()
        self.qt_movefunction.run = self.movefunction
        self.qt_movefunction.start()
        self.checkfuntion = self.checkfunction(self,yt=hwnd)
        self.checkfuntion.checkqsignal.connect(self.changestr)
        self.checkfuntion.start()

    def changestr(self,value):
        self.movestartstate = False
        self.string = self.title_process(value)
        self.qt_movefunction.quit()
        self.qt_movefunction.wait()
        while(self.qt_movefunction.isRunning()):
            pass
        self.qt_movefunction = QtCore.QThread()
        self.qt_movefunction.run = self.movefunction
        self.qt_movefunction.start()
        sleep(0.3)
        self.waiting.wakeAll()

    def movefunction(self):
        self.string=self.title_process(self.string)
        self.ui.music_name.setText(self.string)
        self.movestartstate = True
        self.dpiwidth=self.dpi_pos(self.string)
        if (self.dpiwidth < UI.UI_DISPLAY_WIDTH):
            self.movestartstate = False
            self.ui.music_name.setGeometry(0,0,self.dpiwidth,UI.UI_DISPLAY_HEIGHT)
        while(self.movestartstate):
            self.ui.music_name.setGeometry(0,0,self.dpiwidth,UI.UI_DISPLAY_HEIGHT)
            sleep(1)
            for i in range(self.dpiwidth-UI.UI_DISPLAY_WIDTH):
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
    
    def title_process(self,title:str):
        titlepos=title.find(self.filters[0])
        if titlepos != -1:
            title=title[:titlepos]
        return title
    
    class checkfunction(QtCore.QThread):
        checkqsignal = QtCore.pyqtSignal(str)
        def __init__(self, parent: QObject | None = ... , yt:int = ...) -> None:
            super().__init__(parent)
            self.mutex=parent.mutex
            self.waiting=parent.waiting
            self.yt=yt
            self.checkstartstate = True
        def run(self):
            yt_title = win32gui.GetWindowText(self.yt)
            while(self.checkstartstate):
                yt_title_new = win32gui.GetWindowText(self.yt)
                if (yt_title_new != yt_title):
                    self.mutex.lock()
                    yt_title=yt_title_new
                    self.checkqsignal.emit(yt_title)
                    self.waiting.wait(self.mutex)
                    self.mutex.unlock()

# --------------Controller--------------- #

# --------------Start--------------- #

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pm = QtGui.QPixmap()
    pm.loadFromData(icon.b64decode(icon.img))
    i = QtGui.QIcon()
    i.addPixmap(pm)
    window = MainWindow_controller(i)
    window.show()
    sys.exit(app.exec_())
    
# --------------Start--------------- #