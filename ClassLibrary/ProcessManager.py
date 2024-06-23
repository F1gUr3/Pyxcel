from ClassLibrary.MainScreen import MainScreen


class ProcessManager:
    def StartSession(self):
        ms = MainScreen()
        hasExit = False
        while (not hasExit):
            userInput = input("Folytatás: ");
            if  userInput == "q":
                hasExit = True
            else:
                ms.DisplayContent()

