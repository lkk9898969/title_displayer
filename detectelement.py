class element():
    def __init__(self,text:str,*title:str) -> None:
        '''
        text : A text that show on the button.
        title : filters that remove from window title. It's also a rule of detect.
        '''
        self.text=text
        self.windowtitle=title

