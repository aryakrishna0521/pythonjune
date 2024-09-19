from abc import ABC,abstractmethod

class Editor(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def debug(self):
        pass

class vscode(Editor):
    def open(self):
        print("vscode open")

    
    def execute(self):
        print("vscode execute")

    def debug(self):
        print("vscode close")

vscode_instance=vscode()
vscode_instance.open() 


    
