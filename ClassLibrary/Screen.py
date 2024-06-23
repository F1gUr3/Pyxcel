

class Screen:
    #screenType: (default)0 -> Menu, 1 -> Sheet
    def __init__(self, name, menuItems=None, screenType=0):
        self.currentIndex = 0
        if menuItems is None:
            menuItems = []
        self.name = name
        self.type = screenType
        if(self.type == 0):
            self.menuItems = menuItems
        elif(self.type == 1):
            self.dataGrid = []
    def DisplayContent(self):
        if(self.type == 0):
            for i in range(len(self.menuItems)):
                if(self.currentIndex == i):
                    print("\N{ESC}[31m" + self.menuItems[i] + "\u001b[0m")
                else:
                    print(self.menuItems[i])


        else:
            print("")
    #If WayOfNavigation is + or - we are decrementing and incrementing to navigate
    def NavigateMenu(self, wayOfNavigation):
        print(self.currentIndex)
        if(wayOfNavigation == "+" and self.currentIndex < len(self.menuItems)-1):
            self.currentIndex = self.currentIndex + 1
        elif(wayOfNavigation == "-" and self.currentIndex > 0 ):
            self.currentIndex = self.currentIndex - 1

