from calculator.model import Model
from calculator.service import Service

class Controller:
    def calc(self, num1, num2, opcode):
        model = Model()
        model._num1 = num1
        model._num2 = num2
        model._opcode = opcode
        service = Service(model)
        if opcode == "+":  result = service.add()
        if opcode == "-":  result = service.minus()
        if opcode == "*":  result = service.multiplication()
        if opcode == '/':  result = service.divide()
        return result
