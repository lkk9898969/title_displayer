import pygetwindow,win32gui
class element():
    def __init__(self,text:str,*_filter:str,**kwargs) -> None:
        '''
        text : A text that show on the button.
        _filter : filters that remove from window title. It's also a rule of detect.
        '''
        self.text=text
        self._filter=_filter
        try:
            self.fontfilter=kwargs['frontfilter']
            self.endfilter=_filter[0]
        except KeyError:
            pass
        for i in self._filter:
            if i:
                return
        self.hwnd=win32gui.FindWindowEx(None,None,None,kwargs['fulltitle'])
        self.detect_window=lambda:0

    def detect_window(self):
        ''' return 0 if window not exists'''
        self.hwnd=0
        for i in pygetwindow.getAllTitles():
            flag=True
            for j in self._filter:
                if j in i:
                    continue
                else:
                    flag=False
                    break
            if not flag:
                continue
            self.hwnd = win32gui.FindWindowEx(None,None,None, i)
            return self.hwnd
        return self.hwnd

    def window_title_original(self):
        ''' return window title before filter.\n
        raise exception when:
        1. hwnd=0 (window not exist) ,
        '''
        try:
            if (self.hwnd==0):
                raise ValueError("Cannot find the window.")
        except AttributeError:
            self.hwnd=self.detect_window()
            if (self.hwnd==0):
                raise ValueError("Cannot find the window.")
        title=win32gui.GetWindowText(self.hwnd)
        if title:
            return title
        else:
            self.hwnd=self.detect_window()
            return self.window_title_original()

    def window_title(self):
        ''' return window title after filter.\n
        raise exception when:
        1. hwnd=0 (window not exist) ,
        '''
        title=self.window_title_original()
        try:
            title=title[:title.find(self.endfilter)]
            if self.fontfilter:
                title=title[title.rfind(self.fontfilter)+1:]
        except AttributeError:
            for i in self._filter:
                title=title.replace(i,"")
            title=title.removeprefix(" ").removesuffix(" ")
        return title

