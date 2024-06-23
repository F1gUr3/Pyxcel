from ClassLibrary.Screen import Screen

class MainScreen(Screen):
    def __init__(self):
        menuItems = ["New Sheet", "Open Sheet", "Exit"]
        super().__init__("Main menu", menuItems, 0)


