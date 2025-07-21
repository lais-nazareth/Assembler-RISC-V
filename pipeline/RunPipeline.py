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
        # self.EX = Execute()
        # self.MEM = MemoryAccess()
        # self.WB = WriteBack()

        self.run()


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
        for i in range(10):
            listaFetch, newpc = self.ifetch.runInstructionFetch(self.pc) # retorna o tipo, qual op fazer, indice rs1, indice rs2 e indice rd ou imediato
            print(listaFetch)
            listaDecode = self.id.runInstructionDecode(listaFetch)
            print(listaDecode)

            self.atualInstrucao = listaFetch
            self.converteNome()
            #print(listaFetch)
        # print(self.ex.runExecute())
        # print(self.mem.runMemoryAccess())
        # print(self.wb.runWriteBack())
        



