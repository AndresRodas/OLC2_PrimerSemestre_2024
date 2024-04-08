
class Generator:
    def __init__(self):
        self.Temporal = 0
        self.Label = 0
        self.Code = []
        self.FinalCode = []
        self.Natives = []
        self.FuncCode = []
        self.TempList = []
        self.PrintStringFlag = True
        self.ConcatStringFlag = True
        self.BreakLabel = ""
        self.ContinueLabel = ""
        self.MainCode = False

    def get_code(self):
        return self.Code

    def get_final_code(self):
        return self.FinalCode

    def get_temps(self):
        return self.TempList

    def add_break(self, lvl):
        self.BreakLabel = lvl

    def add_code(self, code):
        self.Code.append(code)

    def add_continue(self, lvl):
        self.ContinueLabel = lvl

    def new_temp(self):
        temp = "t" + str(self.Temporal)
        self.Temporal += 1
        self.TempList.append(temp)
        return temp

    def new_label(self):
        temp = self.Label
        self.Label += 1
        return "L" + str(temp)

    def add_label(self, label):
        if self.MainCode:
            self.Code.append(label + ":\n")
        else:
            self.FuncCode.append(label + ":\n")

    def add_if(self, left, right, operator, label):
        if self.MainCode:
            self.Code.append(f"if({left} {operator} {right}) goto {label};\n")
        else:
            self.FuncCode.append(f"if({left} {operator} {right}) goto {label};\n")

