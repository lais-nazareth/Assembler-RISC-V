from pipeline.InstructionFetch import *
from pipeline.InstructionDecode import *
from pipeline.Execute import *
from pipeline.MemoryAccess import *
from pipeline.WriteBack import *


class RunPipeline():
    def __init__(self, binaryfile):
        # cria as instancias das classes de cada etapa
        self.IF = InstructionFetch(binaryfile)
        # self.ID = InstructionDecode()
        # self.EX = Execute()
        # self.MEM = MemoryAccess()
        # self.WB = WriteBack()

        self.run()

    def run(self):
        
        print(self.IF.runInstructionFetch())
        print(self.ID.runInstructionDecode())
        print(self.EX.runExecute())
        print(self.MEM.runMemoryAccess())
        print(self.WB.runWriteBack())
        



