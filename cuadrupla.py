class qBlock:
    def __init__(self, label, parent = None):
        self.label = label
        self.parent = parent
        self.children = []
        self.quadruples = []
        if parent:
            parent.children.append(self)

class Quadruple:
    def __init__(self, operator, operand1, operand2, result):
        self.operator = operator
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
    def __str__(self):
        return f'{self.operator} {self.operand1} {self.operand2} {self.result}'
    