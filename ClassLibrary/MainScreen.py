import keyboard
from ClassLibrary.CreateNewSheet import CreateNewSheet
from ClassLibrary.Screen import Screen

class MainScreen(Screen):
    def __init__(self):
        menuItems = ["New Sheet", "Open Sheet", "Exit"]
        super().__init__("Main menu", menuItems, 0)

    def QuitIsPressed(self):
        if(self.currentIndex == 2 and keyboard.is_pressed("enter")):
            return True
    def NewSheetPressed(self):
        if(self.currentIndex == 0 and keyboard.is_pressed("enter")):
            cns = CreateNewSheet()
            return cns


