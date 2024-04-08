
class Ast():
    def __init__(self):
        self.instructions = []
        self.console = ""
        self.errors = []

    def setConsole(self, content):
        self.console += content + "\n"
    
    def getConsole(self):
        return self.console

    def addInstructions(self, instructions):
        self.instructions += instructions
    
    def getInstructions(self):
        return self.instructions
    
    def setErrors(self, errors):
        self.errors.append(errors)
    
    def getErrors(self):
        return self.errors