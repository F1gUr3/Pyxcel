import time

from ClassLibrary.MainScreen import MainScreen
from ClassLibrary.SystemTools import clear
import keyboard

class ProcessManager:

    def __init__(self):
        self.currentWindow = MainScreen()
        self.hasExit = False
    def PushWindow(self, typeOfWindow):
        self.currentWindow = typeOfWindow

    def StartSession(self):
        self.currentWindow = MainScreen()

        while not self.hasExit:
            if keyboard.is_pressed("up"):
                self.currentWindow.NavigateMenu("-")
                time.sleep(0.2)  # Delay to prevent multiple key presses being registered at once
            elif keyboard.is_pressed("down"):
                self.currentWindow.NavigateMenu("+")
                time.sleep(0.2)

            if self.currentWindow.name == "Main menu":
                self.hasExit = self.currentWindow.QuitIsPressed()
                new_window = self.currentWindow.NewSheetPressed()
                if new_window != None:
                    self.PushWindow(new_window)
            elif self.currentWindow.name == "Create New Sheet":
                if self.currentWindow.Back():
                    self.PushWindow(MainScreen())
                else:
                    self.currentWindow.CreateNewSheet()

            clear()
            self.currentWindow.DisplayContent()
            time.sleep(0.1)  # Small delay to prevent high CPU usage




