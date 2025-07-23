from pipeline.InstructionFetch import *

class DeteccaoHazards:
    def __init__(self, forwarding_enabled=False, binaryfile: str = None, asmfile: str = None):
        self.forwarding_enabled = forwarding_enabled
        self.binaryfile = binaryfile
        self.asmfile = asmfile
        self.filelist = None
        self.listainstrucoesfetch = []

        # self.ifetch = InstructionFetch(binaryfile=self.binaryfile, asmfile=self.asmfile)
        self.pc = 0

        # if self.binaryfile:
        #     fp = open(self.binaryfile, "r")
        #     self.filelist = fp.readlines()
            
            
        #     # self.filelist = self.detect()
        # else:
        #     fp = open(self.asmfile, "r")
        #     self.filelist = fp.readlines()

            # self.filelist = self.detect()

    def detect(self):
        newpc = 0
       
        pos_c_bolha = []

        while newpc != -1:
            listaFetch, newpc = self.ifetch.runInstructionFetch(self.pc)
            self.pc = newpc
            if newpc != -1:
                self.listainstrucoesfetch.append(listaFetch)


        # print(self.listainstrucoesfetch)

        
        for i in range(len(self.listainstrucoesfetch)):
            instr_atual = self.listainstrucoesfetch[i]
            if instr_atual == ['I', 'addi', 0, 0,0 ]:
                continue
            if instr_atual[0] == 'R' or instr_atual[0] == 'I':
                for j in range(1, 5):
                        bolhas = [['I', "addi", 0, 0, 0]] * (4-(j-i))
                        if self.listainstrucoesfetch[j][0] == 'R':
                            if instr_atual[2] == self.listainstrucoesfetch[j][3] or instr_atual[2] == self.listainstrucoesfetch[j][4]:
                                self.listainstrucoesfetch = self.listainstrucoesfetch[:i+1] + bolhas  + self.listainstrucoesfetch[i+1:]
                        if self.listainstrucoesfetch[j][0] == 'I':
                            if instr_atual[2] == self.listainstrucoesfetch[j][3]:
                                self.listainstrucoesfetch = self.listainstrucoesfetch[:i+1] + bolhas + self.listainstrucoesfetch[i+1:]
                        if self.listainstrucoesfetch[j][0] == 'S':
                            if instr_atual[2] == self.listainstrucoesfetch[j][2] or instr_atual[2] == self.listainstrucoesfetch[j][3]:
                                self.listainstrucoesfetch = self.listainstrucoesfetch[:i+1] + bolhas + self.listainstrucoesfetch[i+1:]
                        if self.listainstrucoesfetch[j][0] == 'B':
                            if instr_atual[2] == self.listainstrucoesfetch[j][2] or instr_atual[2] == self.listainstrucoesfetch[j][3]:
                                self.listainstrucoesfetch = self.listainstrucoesfetch[:i+1] + bolhas + self.listainstrucoesfetch[i+1:]
            if instr_atual[0] == 'S':
                for j in range(1, 5):
                    bolhas = [['I', "addi", 0, 0, 0]]* (4-(j-i))
                    if self.listainstrucoesfetch[j][1] == 'lw':
                            self.listainstrucoesfetch = self.listainstrucoesfetch[:i+1] + bolhas + self.listainstrucoesfetch[i+1:]
                
                    
                        

            print(self.listainstrucoesfetch)
            


            # prox_1 = self.listainstrucoesfetch[i+1]

        # detecta no self.listainstrucoesfetch onde vai precisar de bolha
        # grava as posicoes pra adicionar bolha em um vetor

        # if not instr_atual or instr_atual[0] == 'B':
        #     return False  # ignorar branch por enquanto

        # using_regs = []
        # if instr_atual[0] == 'R':
        #     using_regs = [instr_atual[3], instr_atual[4]]
        # elif instr_atual[0] == 'I':
        #     using_regs = [instr_atual[3]]
        # elif instr_atual[0] == 'S':
        #     using_regs = [instr_atual[3]]

    def escreveNoArquivo(self, asm: bool):

        if asm:
            fp = open("temporario.asm", "w")

            for line in self.filelist:
                fp.write(line)
        else:
            fp = open("temporario.binary", "w")

            for line in self.filelist:
                fp.write(line)