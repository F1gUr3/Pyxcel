from ClassLibrary.MainScreen import MainScreen
from ClassLibrary.SystemTools import clear
class ProcessManager:
    def StartSession(self):
        ms = MainScreen()
        hasExit = False
        while (not hasExit):
            userInput = input("Folytatás: ");
            if  userInput == "q":
                hasExit = True
            else:
                clear()
                ms.DisplayContent()


