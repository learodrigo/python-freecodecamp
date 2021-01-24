from Chef import Chef


class ChineseChef(Chef):
    def __init__(self):
        self.name = "Chinese chef"

    def make_special_dish(self):
        print(self.name, "thinks about making orange chicken")

    def make_fried_rice(self):
        print(self.name, "thinks about making fried rice")
