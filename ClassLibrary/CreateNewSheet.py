from ClassLibrary.Screen import Screen


class CreateNewSheet(Screen):
    def __init__(self):
        menuItems = ["New Sheet",  "Back"]
        super().__init__("Create New Sheet", menuItems, 0)