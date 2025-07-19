from riscv_data.instructions import Instructions
from riscv_data.registers import Registers
from pipeline.InstructionFetch import InstructionFetch

class Run:
    def __init__(self, arq):
        self.arq = open(arq, "r")
        self.PC = 0
        self.start()

    def start(self):
        if self.arq.readline().split()[0] == ".data":
            self.readData()
        else:
            self.readText()

    def readData(self):
        try:
            while True:
                line = self.arq.readline().split()
                if line[0] == ".text":
                    self.readText()
        except EOFError:
            pass
    
    
    def readText(self):
        try:
            self.PC = self.arq.tell()
            while True:

                line = self.arq.readline().split()

        except EOFError:
            pass
        
    def runInstruction(self):
        self.PC = InstructionFetch.instructionFetch(self.PC)