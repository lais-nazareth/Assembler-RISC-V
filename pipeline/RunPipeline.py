from pipeline.InstructionFetch import *
from pipeline.InstructionDecode import *
from pipeline.Execute import *
from pipeline.MemoryAccess import *
from pipeline.WriteBack import *


class RunPipeline():
    def __init__(self, filename: str):
        self.binaryfile = None
        self.asmfile = None
        self.filetype = None
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

    def run(self):
        for i in range(10):
            listaFetch, newpc = self.ifetch.runInstructionFetch(self.pc) # retorna o tipo, qual op fazer, indice rs1, indice rs2 e indice rd ou imediato
            print(listaFetch)
            listaDecode = self.id.runInstructionDecode(listaFetch)
            print(listaDecode)
        # print(self.ex.runExecute())
        # print(self.mem.runMemoryAccess())
        # print(self.wb.runWriteBack())
        



