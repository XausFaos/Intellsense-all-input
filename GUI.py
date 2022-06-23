import eel
import win32gui
import win32con
import threading

sizeX = 300
sizeY = 300
startX = 0
startY = 0


class GUI:

    flagMovePos = True
    
    def __init__(self, inputsObj):
        inputsObj.SetGui(self)
        eel.init('web')
        threading.Thread(target=self.StartAfterLoadGui, args=(), daemon=True).start()
        eel.start('main.html', size=(sizeX, sizeY))


    def StartAfterLoadGui(self):
        self.window = 0
        while self.window == 0:    
            self.GetWindow()
            self.SetAlwaysOnTop()
            
        print("Loading finished")


    def GetWindow(self):
        self.window = win32gui.FindWindowEx(None, None, None, "Board")


    def SetAlwaysOnTop(self):
        if self.window == 0:
            return

        win32gui.SetWindowPos(self.window, win32con.HWND_TOPMOST, startX, startY, startX + sizeX, startY + sizeY, 0)


    def SetWindowPosition(self, x, y):
        if self.window == 0 and not self.flagMovePos:
            return
        print(x,y, x + sizeX, y + sizeY)
        win32gui.SetWindowPos(self.window, win32con.HWND_TOPMOST, x, y, x + sizeX, y + sizeY, 0)