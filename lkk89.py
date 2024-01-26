from PyQt5.QtGui import QContextMenuEvent
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from detectelement import element as detectelement

import icon
import pygetwindow as gw
import UI
# --------------Controller--------------- #
# shell = win32com.client.Dispatch("WScript.Shell")
# ------------Main Controller------------ #
class MainWindow_controller(QtWidgets.QStackedWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUI()
        self.setup_control()
        self.switch_to_selecting()

    def setupUI(self):
        pm = QtGui.QPixmap()
        pm.loadFromData(icon.b64decode(icon.img))
        i = QtGui.QIcon()
        i.addPixmap(pm)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.setWindowTitle("Youtube Title Displayer")
        self.setWindowIcon(i)
    
    def setup_control(self):
        self.mousemove=False
    
    def selecting_button_init(self):
        '''
        initial the button and element.
        Note that the first element.windowtitle will be the cutoff point for the title to display.
        '''
        for i in self.datainit():
            self.addbutton(i)
        button=self.selecting.addbutton("自行選擇視窗")
        button.clicked.connect(self.switch_to_titlelist)

    def datainit(self) -> list[detectelement]:
        _result=[]
        i=detectelement("Youtube"," - YouTube"," - Microsoft​ Edge",frontfilter="")
        _result.append(i)
        i=detectelement("VLC"," - VLC",frontfilter="")
        _result.append(i)
        return _result

    def addbutton(self,element:detectelement):
        button=self.selecting.addbutton(element.text)
        button.clicked.connect(lambda state,element=element:self.switch_to_detecting(element))
    
    def switch_to_selecting(self):
        self.selecting=selecting_controller(self)
        self.selecting_button_init()
        index=self.addWidget(self.selecting)
        self.setCurrentIndex(index)
        pass
    
    def switch_to_titlelist(self):
        self.titlelist=TitlelistWindow_Controller(self)
        self.titlelist.signal.connect(self.switch_to_titlefilter)
        index=self.addWidget(self.titlelist)
        self.setCurrentIndex(index)
    
    def switch_to_titlefilter(self,title:str):
        self.titlefilter=TitlefilterWindow_Controller(self,title)
        self.titlefilter.signal.connect(self.switch_to_display)
        index=self.addWidget(self.titlefilter)
        self.setCurrentIndex(index)

    def switch_to_detecting(self,element:detectelement):
        self.dectecting=detecting_controller(self,element,lambda element=element:self.switch_to_display(element))
        index=self.addWidget(self.dectecting)
        self.setCurrentIndex(index)

    def switch_to_display(self,element:detectelement):
        
        self.displaying = DisplayWindow_controller(self,element)
        index=self.addWidget(self.displaying)
        # self.showMinimized()
        self.setCurrentIndex(index)
        self.show()
        self.showMaximized()
        self.showNormal()
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setup_Mainwindow()

    def setup_Mainwindow(self):
        self.Action=QtWidgets.QAction("離開",self)
        self.Action.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_TitleBarCloseButton))
        self.Action.setShortcut(QtCore.Qt.Modifier.CTRL + QtCore.Qt.Key.Key_X)
        self.Action.triggered.connect(self.close)
        self.Stayontop=QtWidgets.QAction("保持在最上層",self)
        self.Stayontop.setCheckable(True)
        self.Stayontop.triggered.connect(self.stayontop_toggle)
        self.addAction(self.Stayontop)
        self.addAction(self.Action)
        self.oldPos = self.pos()
        self.mousePressEvent=self.drggable_mousePressEvent
        self.mouseReleaseEvent=self.drggable_mouseReleaseEvent
        self.mouseMoveEvent=self.drggable_mouseMoveEvent
        self.contextMenuEvent=self.drggable_contextMenuEvent
    
    def stayontop_toggle(self):
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint,self.Stayontop.isChecked())
        self.show()
    
    def drggable_contextMenuEvent(self, a0: QContextMenuEvent | None) -> None:
        menu = QtWidgets.QMenu()
        menu.addAction(self.Stayontop)
        menu.addAction(self.Action)
        menu.exec_(a0.globalPos())
        return super().contextMenuEvent(a0)

    def drggable_mousePressEvent(self, a0: QtGui.QMouseEvent | None) -> None:
        if(a0.button()==QtCore.Qt.MouseButton.LeftButton):
            self.oldPos = a0.globalPos()
            self.mousemove=True
        return super().mousePressEvent(a0)
    
    def drggable_mouseReleaseEvent(self, a0: QtGui.QMouseEvent | None) -> None:
        self.mousemove=False
        return super().mousePressEvent(a0)

    def drggable_mouseMoveEvent(self, a0: QtGui.QMouseEvent | None) -> None:
        if self.mousemove:
            delta = QtCore.QPoint (a0.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = a0.globalPos()
        return super().mouseMoveEvent(a0)
    
    def closeEvent(self, a0: QtGui.QCloseEvent | None) -> None:
        self.hide()
        try:
            self.dectecting.timer.stop()
            self.displaying.checktimer.stop()
            self.displaying.movethreadquit()
        except AttributeError:
            pass
        return super().closeEvent(a0)

# ----------Selecting Controller--------- #
class selecting_controller(QtWidgets.QWidget,UI.Ui_Selecting_Client):
    def __init__(self,MainWindow) -> None:
        super().__init__(MainWindow)
        self.setupUi(self)

    def addbutton(self,text:str):
        return self.uiaddbutton(text)

# ----------Detecting Controller--------- #
class detecting_controller(QtWidgets.QWidget,UI.Ui_Detecting):
    detectingsignal=QtCore.pyqtSignal()
    def __init__(self,MainWindow,element:detectelement,func):
        '''
        func : the fuction that detectingsignal connect.
        detectingsignal will emit when window detected.
        '''
        super().__init__(MainWindow) # in python3, super(Class, self).xxx = super().xxx
        self.setupUi(self,element.text)
        self.setup_control(element,func)
    
    def setup_control(self,element:detectelement,func):
        # self.setWindowIcon(i)
        self.detectingsignal.connect(func)
        self.element=element
        self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.detect)
        self.timer.start(1000)
    
    def detect(self):
        yt=self.element.detect_window()
        if yt:
            self.detectingsignal.emit()
            self.timer.stop()

# ---------DisplayWindow Controller--------- #
class DisplayWindow_controller(QtWidgets.QWidget,UI.Ui_display_music_name):
    def __init__(self,parent,element:detectelement):
        super().__init__(parent) # in python3, super(Class, self).xxx = super().xxx
        self.setupUi(self)
        self.setup_control(element)

    def setup_control(self,element:detectelement):
        self.dplength=20
        # self.setWindowIcon(i)
        self.element = element
        self.check_yt_title = self.element.window_title_original()
        self.check_yt_title_new = self.element.window_title_original()
        self.qt_movefunction = QtCore.QThread(self)
        self.qt_movefunction.run = self.movefunction
        self.qt_movefunction.start()
        self.checktimer = QtCore.QTimer(self)
        self.checktimer.timeout.connect(self.checkfunc)
        self.checktimer.start(200)
    
    def checkfunc(self):
        self.check_yt_title_new = self.element.window_title_original()
        if (self.check_yt_title_new != self.check_yt_title):
            self.check_yt_title=self.check_yt_title_new
            self.changestr()
    
    def changestr(self):
        self.movethreadquit()
        self.qt_movefunction = QtCore.QThread(self)
        self.qt_movefunction.run = self.movefunction
        self.qt_movefunction.start()
        sleep(0.3)

    def movefunction(self):
        self.string=self.element.window_title()
        self.music_name.setText(self.string)
        self.movestartstate = True
        self.dpiwidth=self.dpi_pos(self.string)
        if (self.dpiwidth < UI.UI_DISPLAY_WIDTH):
            self.movestartstate = False
            self.music_name.setGeometry(0,0,self.dpiwidth,UI.UI_DISPLAY_HEIGHT)
        while(self.movestartstate):
            self.music_name.setGeometry(0,0,self.dpiwidth,UI.UI_DISPLAY_HEIGHT)
            sleep(1)
            for i in range(self.dpiwidth-UI.UI_DISPLAY_WIDTH):
                if not (self.movestartstate):
                    return
                sleep(0.03)
                try:
                    self.music_name.move(-i,0)
                except RuntimeError:
                    self.movestartstate=False
                    return
            sleep(1)
    
    def dpi_pos(self,text:str):
        return self.qfontmetrics.width(text)

    def movethreadquit(self):
        self.movestartstate = False
        self.qt_movefunction.quit()
        self.qt_movefunction.wait()
        while(self.qt_movefunction.isRunning()):
            pass

    

#------------Title list Controller-----------#
class TitlelistWindow_Controller(QtWidgets.QWidget,UI.Ui_titlelist):
    signal=QtCore.pyqtSignal(str)
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None:
        super().__init__(parent)
        # self.ui=UI.Ui_titlelist()
        # self.ui.setupUi(self)
        self.setupUi(self)
        self.setup_control()
    
    def setup_control(self):
        # self.OK = QtWidgets.QPushButton()
        self.OK.clicked.connect(self.OKbutton_clicked)
        self.refresh.clicked.connect(self.Refreshbutton_clicked)
        self.windowstitles=[i for i in gw.getAllTitles() if i!=""]
        self.titlelist.addItems(self.windowstitles.copy())

    def Refreshbutton_clicked(self):
        self.refresh.setEnabled(False)
        self.titlelist.clear()
        self.windowstitles=[i for i in gw.getAllTitles() if i!=""]
        self.titlelist.addItems(self.windowstitles.copy())
        self.refreshtimer = QtCore.QTimer(self)
        self.refreshtimer.singleShot(1000,lambda:self.refresh.setEnabled(True))
    
    def OKbutton_clicked(self):
        # self.titlelist = QtWidgets.QListWidget()
        item=self.titlelist.currentItem()
        if item.isSelected():
            title=item.data(0)
            self.signal.emit(title)
        else:
            QtWidgets.QMessageBox(self).critical(self,'Error','請選擇視窗標題。')

#------------Title filter Controller-----------#
class TitlefilterWindow_Controller(QtWidgets.QWidget,UI.Ui_titlefilter):
    signal=QtCore.pyqtSignal(detectelement)
    def __init__(self, parent: QtWidgets.QWidget | None , title:str) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setup_control(title)
        # self.ui=UI.Ui_titlefilter()
    
    def setup_control(self,title:str):
        self.titleEdit.setText(title)
        self.original_title=title
        self.Enter.clicked.connect(self.Enterclicked)
        self.titleEdit.setReadOnly(False)
    
    def Enterclicked(self):
        title=self.titleEdit.toPlainText()
        if self.original_title.find(title) == -1 :
            QtWidgets.QMessageBox(self).critical(self,'Error',"標題不符合")
            self.titleEdit.setText(self.original_title)
        else:
            if title==self.original_title:
                newelement=detectelement("自訂",'',fulltitle=title)
                self.signal.emit(newelement)
                return
            title_filter=self.original_title.replace(title,"{}",1)
            title_filters=title_filter.split("{}")
            newelement=detectelement("自訂",title_filters[0],title_filters[1])
            self.signal.emit(newelement)

        
    

# --------------Controller--------------- #

# --------------Start--------------- #

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())
    
# --------------Start--------------- #