from pipeline.InstructionFetch import *
from pipeline.InstructionDecode import *
from pipeline.Execute import *
from pipeline.MemoryAccess import *
from pipeline.WriteBack import *
from riscv_data import registers


class RunPipeline():
    def __init__(self, filename: str):
        self.binaryfile = None
        self.asmfile = None
        self.filetype = None
        
        self.value_regs = [0] * 32
        self.memory = [None] * 20

        self.listaInstrucoes = [] #Lista que contem as strings com o comando de cada instrucao, sem considerar label
        self.listaRegs = Registers().registers
        self.atualInstrucao = []
        if filename[-4:] == ".asm":
            self.asmfile = filename
            self.filetype = "asm"
        else:
            self.binaryfile = filename
            self.filetype = "bin"

        self.pc = 0

        # cria as instancias das classes de cada etapa
        self.ifetch = InstructionFetch(binaryfile=self.binaryfile, asmfile=self.asmfile)
        self.id = InstructionDecode(self.filetype)
        self.ex = Execute()
        self.mem = MemoryAccess()
        self.wb = WriteBack()

        self.regifid = None
        self.regidex = None
        self.regexmem = None
        self.regmemwb = None

        self.c = 0

        # self.run()

    def converteNome(self):
        # Criar dicionário reverso
        index_to_name = {v: k for k, v in self.listaRegs.items()}

        tipo = self.atualInstrucao[0]
        if tipo == 'R':  # ['R', opcode, rd, rs1, rs2]
            rd_name  = index_to_name[self.atualInstrucao[2]]
            rs1_name = index_to_name[self.atualInstrucao[3]]
            rs2_name = index_to_name[self.atualInstrucao[4]]
            self.listaInstrucoes.append(f"{self.atualInstrucao[1]} {rd_name}, {rs1_name}, {rs2_name}")

        elif tipo in ('I', 'B'):  # ['I', opcode, rd, rs1, imm] ou ['B', opcode, rs1, rs2, imm]
            if self.atualInstrucao[1] == "addi" and self.atualInstrucao[2] == 0 and self.atualInstrucao[3] == 0 and self.atualInstrucao[4] == 0:
                self.listaInstrucoes.append("nop")
            else:
                rd_name  = index_to_name[self.atualInstrucao[2]]
                rs1_name = index_to_name[self.atualInstrucao[3]]
                imm      = self.atualInstrucao[4]
                self.listaInstrucoes.append(f"{self.atualInstrucao[1]} {rd_name}, {rs1_name}, {imm}")

        elif tipo == 'S':  # ['S', opcode, rd, rs1, imm]
            rs2_name = index_to_name[self.atualInstrucao[2]]
            rs1_name = index_to_name[self.atualInstrucao[3]]
            imm      = self.atualInstrucao[4]
            self.listaInstrucoes.append(f"{self.atualInstrucao[1]} {rs2_name}, {imm}({rs1_name})")

        elif tipo == 'J':  # ['J', opcode, rd, imm]
            rd_name = index_to_name[self.atualInstrucao[2]]
            imm     = self.atualInstrucao[3]
            self.listaInstrucoes.append(f"{self.atualInstrucao[1]} {rd_name}, {imm}")

        #print(self.listaInstrucoes[-1])
        return self.listaInstrucoes
    
    def run(self):
        # print(self.memory)
        # print(self.value_regs)
        while True: # ciclos
            oldpc = self.pc
            listaFetch, newpc = self.ifetch.runInstructionFetch(self.pc) # retorna o tipo, qual op fazer, indice rs1, indice rs2 e indice rd ou imediato
            if newpc == -1:
                if self.c < 5:
                # print(self.listaInstrucoes)
                    self.regifid = ['I', 'addi', 0, 0, 0]
                    self.c += 1
                else:
                    return
                # return
            
            if self.regifid:
                listaDecode = self.id.runInstructionDecode(self.regifid, self.value_regs)

            # if listaFetch != ['I', 'addi', 0, 0, 0]:
                # print(listaFetch)

            if newpc != -1:
                self.atualInstrucao = listaFetch
                self.converteNome()
                self.pc = newpc
            # listaDecode = self.id.runInstructionDecode(listaFetch, self.value_regs)
            # print(listaDecode)

            if self.regidex:
                if self.asmfile:
                    listaExecute, pcexec = self.ex.runExecute(self.regidex, newpc-2)
                else:
                    listaExecute, pcexec = self.ex.runExecute(self.regidex, oldpc-2)
                if listaExecute[0] == 'B':
                    if listaExecute[2]:
                        self.pc = pcexec
                if listaExecute[0] == 'J':
                    self.pc = pcexec
            
            # print(self.pc)

            # if self.regifid:
            #     self.regidex = listaDecode

            # self.regifid = listaFetch

            if self.regexmem:
                if self.regexmem[1] == "lw" or self.regexmem[1] == "sw":
                    listaExecToMem = self.regexmem[:]
                    listaExecToMem[2] = self.value_regs[self.regexmem[2]]
                    wordRead = self.mem.runMemoryAccess(listaExecToMem, self.memory)
                    self.regexmem[-1] = wordRead
                    self.value_regs = self.wb.runWriteBack(self.regexmem, self.value_regs)
                else:
                    self.mem.runMemoryAccess(self.regexmem, self.value_regs)
            
            # if self.regidex:
            #     self.regexmem = listaExecute

            # print(self.memory)
            if self.regmemwb:
                self.value_regs = self.wb.runWriteBack(self.regmemwb, self.value_regs)

            if self.regexmem:
                self.regmemwb = self.regexmem

            if self.regidex:
                self.regexmem = listaExecute
            
            if self.regifid:
                self.regidex = listaDecode

            self.regifid = listaFetch

            
                # print(self.value_regs)

    def next(self): 
        oldpc = self.pc
        listaFetch, newpc = self.ifetch.runInstructionFetch(self.pc) # retorna o tipo, qual op fazer, indice rs1, indice rs2 e indice rd ou imediato
        if newpc == -1:
            if self.c < 5:
            # print(self.listaInstrucoes)
                self.regifid = ['I', 'addi', 0, 0, 0]
                self.c += 1
            else:
                return
            # return
        
        if self.regifid:
            listaDecode = self.id.runInstructionDecode(self.regifid, self.value_regs)

        # print(listaFetch)
        if newpc != -1:
            self.atualInstrucao = listaFetch
            self.converteNome()
            self.pc = newpc
        # listaDecode = self.id.runInstructionDecode(listaFetch, self.value_regs)
        # print(listaDecode)

        if self.regidex:
            if self.asmfile:
                listaExecute, pcexec = self.ex.runExecute(self.regidex, newpc-2)
            else:
                listaExecute, pcexec = self.ex.runExecute(self.regidex, oldpc-2)
            if listaExecute[0] == 'B':
                if listaExecute[2]:
                    self.pc = pcexec
            if listaExecute[0] == 'J':
                self.pc = pcexec
        # print(self.pc)

        # if self.regifid:
        #     self.regidex = listaDecode

        # self.regifid = listaFetch

        if self.regexmem:
            if self.regexmem[1] == "lw" or self.regexmem[1] == "sw":
                listaExecToMem = self.regexmem[:]
                listaExecToMem[2] = self.value_regs[self.regexmem[2]]
                wordRead = self.mem.runMemoryAccess(listaExecToMem, self.memory)
                self.regexmem[-1] = wordRead
                self.value_regs = self.wb.runWriteBack(self.regexmem, self.value_regs)
            else:
                self.mem.runMemoryAccess(self.regexmem, self.value_regs)
        
        # if self.regidex:
        #     self.regexmem = listaExecute

        # print(self.memory)
        if self.regmemwb:
            self.value_regs = self.wb.runWriteBack(self.regmemwb, self.value_regs)

        if self.regexmem:
            self.regmemwb = self.regexmem

        if self.regidex:
            self.regexmem = listaExecute
        
        if self.regifid:
            self.regidex = listaDecode

        self.regifid = listaFetch
    # def next(self): #SEM WHILE TRUE, PARA IR 1 POR 1...
    #     oldpc = self.pc
    #     listaFetch, newpc = self.ifetch.runInstructionFetch(self.pc) # retorna o tipo, qual op fazer, indice rs1, indice rs2 e indice rd ou imediato
    #     if newpc == -1:
    #         print("EXECUCAO CONCLUIDA.")
    #         #print(self.listaInstrucoes)
    #         return
    #     print(listaFetch)
    #     self.atualInstrucao = listaFetch
    #     self.converteNome()
    #     self.pc = newpc
    #     listaDecode = self.id.runInstructionDecode(listaFetch, self.value_regs)
    #     print(listaDecode)
    #     if self.asmfile:
    #         listaExecute, pcexec = self.ex.runExecute(listaDecode, newpc)
    #     else:
    #         listaExecute, pcexec = self.ex.runExecute(listaDecode, oldpc)
    #     if listaExecute[0] == 'B':
    #         if listaExecute[2]:
    #             self.pc = pcexec
    #     if listaExecute[0] == 'J':
    #         self.pc = pcexec
    #     print(self.pc)
    #     if listaExecute[1] == "lw" or listaExecute[1] == "sw":
    #         listaExecToMem = listaExecute[:]
    #         listaExecToMem[2] = self.value_regs[listaExecute[2]]
    #         wordRead = self.mem.runMemoryAccess(listaExecToMem, self.memory)
    #         listaExecute[-1] = wordRead
    #         self.value_regs = self.wb.runWriteBack(listaExecute, self.value_regs)
    #     else:
    #         self.mem.runMemoryAccess(listaExecute, self.value_regs)
    #         # print(self.memory)
    #     self.value_regs = self.wb.runWriteBack(listaExecute, self.value_regs)
    #     #print(self.value_regs)
