class ProcessManager:
    def StartSession(self):
        hasExit = False
        while (not hasExit):
            if (input("Folytatja? I/N: ") == "I"):
                print("Folytatva")
            else:
                hasExit = True