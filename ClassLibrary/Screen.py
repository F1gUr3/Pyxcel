class Screen:
    #0 -> Menu, 1 -> Sheet
    def __init__(self, name, menuItems= [], screenType=0):
        self.name = name
        self.type = screenType
        if(self.type == 0):
            self.menuItems = menuItems
        elif(self.type == 1):
            self.dataGrid = []
    def DisplayContent(self):
        if(self.type == 0):
            for i in range(self.menuItems.count(self)):
                print(self.menuItems[i])
        else:
            print("")
