from riscv_data.registers import Registers

class WriteBack:
    
    def __init__(self):
        self.memToReg = 0

    def runWriteBack(self, lista, value_regs): # assumindo que a lista seja [tipo, mnemonico, posicao do registrador a escrever, valor a escrever]
        if lista[0] != 'B' and lista[0] != 'S':
            if lista[2] != 0:
                value_regs[lista[2]] = lista[3]

        return value_regs