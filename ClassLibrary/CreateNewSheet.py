from ClassLibrary.Screen import Screen
import keyboard


class CreateNewSheet(Screen):
    def __init__(self):
        menuItems = ["New Sheet",  "Back"]
        super().__init__("Create New Sheet", menuItems, 0)
    def Back(self):
        if(self.currentIndex == 1 and keyboard.read_key("enter") ):
            return True