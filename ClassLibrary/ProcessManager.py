import time

from ClassLibrary.MainScreen import MainScreen
from ClassLibrary.SystemTools import clear
import keyboard
class ProcessManager:

    def StartSession(self):
        ms = MainScreen()
        hasExit = False

        while not hasExit:
            if keyboard.is_pressed("up"):
                ms.NavigateMenu("-")
                time.sleep(0.2)  # Delay to prevent multiple key presses being registered at once
            elif keyboard.is_pressed("down"):
                ms.NavigateMenu("+")
                time.sleep(0.2)
            elif keyboard.is_pressed("q"):
                hasExit = True

            clear()
            ms.DisplayContent()
            time.sleep(0.1)  # Small delay to prevent high CPU usage




