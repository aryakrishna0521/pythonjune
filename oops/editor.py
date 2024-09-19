class Editor:
    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendor

    def open(self):
        print(f"{self.name} open")

    def execute(self):
        print(f"{self.name} execute")


class vscode(Editor):
    def __init__(self,name,vendor):
        super().__init__(name,vendor)

class pycharm(Editor):
    def __init__(self,name,vendor):
        super().__init__(name,vendor)

vscode_instance=vscode("vscode","bbg")
vscode_instance.open()
vscode_instance.execute()

pycharm_instance=pycharm("pycharm","jetbrains")
pycharm_instance.open()
pycharm_instance.execute()
