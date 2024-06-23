from ClassLibrary.Screen import Screen
import keyboard
from ClassLibrary.SystemTools import clear
import os


class CreateNewSheet(Screen):
    def __init__(self):
        menuItems = ["New Sheet",  "Back"]
        super().__init__("Create New Sheet", menuItems, 0)
    def Back(self):
        if(self.currentIndex == 1 and keyboard.is_pressed("enter")):
            return True
    def CreateNewSheet(self):
        if(self.currentIndex == 0 and keyboard.is_pressed("enter")):
            clear()
            FileName = input("Adja meg a létrehozni kívánt fájl nevét: ")
            with open("workSheets/"+FileName + ".csv", "w") as newSheet:
                newSheet.close()
