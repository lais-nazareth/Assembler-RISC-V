from riscv_data.instructions import Instructions
from riscv_data.registers import Registers
#tipo, mnemonico, rd, rs1, rs2(or imm)

#L: amanha eu vou na igreja pedir a deus pra tocar o coração da cheng xu

#A: amem vc vai passar

#L: obg amanda

#ME: vai dar tudo certo Lais!

# Guilherme da hora: 會失敗

#L: nihao


class InstructionDecode:
    def __init__(self, fileType: str):
        self.fileType = fileType
        self.type = None
        self.instruction = None
        self.rd = 0
        self.rs1 = 0
        self.rs2orimm = 0
        # self.pc

    def runInstructionDecode(self, listaFetch):
        if self.fileType == "asm":
            return self.runInstructionDecodeAsm(listaFetch)
        else:
            return self.runInstructionDecodeBinary(listaFetch)        

    def runInstructionDecodeAsm(self, listaFetch):

        if (not listaFetch):
            return None

        self.type = listaFetch[0]
        self.instruction = listaFetch[1]
        # self.rd = listaFetch[2]
        # self.rs1 = listaFetch[3]
        # self.rs2orimm = listaFetch[4]

        

        if (self.type == 'R'):
            self.rd = listaFetch[2]
            self.rs1 = listaFetch[3]
            self.rs2orimm = listaFetch[4]
            rd = Registers.value_regs[self.rd]
            rs1 = Registers.value_regs[self.rs1]
            rs2 = Registers.value_regs[self.rs2]
            return ['R', listaFetch[1], self.rd, rs1, rs2]

        if (self.type == 'I'):
            if self.instruction != "jalr":
                self.rd = listaFetch[2]
                self.rs1 = listaFetch[3]
                self.rs2orimm = listaFetch[4]
                rd = Registers.value_regs[self.rd]
                rs1 = Registers.value_regs[self.rs1]
                imm = self.rs2orimm
                return ['I', listaFetch[1], self.rd, rs1, imm]
        
        if (self.type == 'J'):
            self.rd = listaFetch[2]
            self.rs2orimm = listaFetch[3]
            rd = Registers.value_regs[self.rd]
            imm = self.rs2orimm

            return ['J', listaFetch[1], self.rd, imm]
        
        if (self.type == 'S'):
            self.rd = listaFetch[2]
            self.rs1 = listaFetch[3]
            self.rs2orimm = listaFetch[4]
            rd = Registers.value_regs[self.rd]
            rs1 = Registers.value_regs[self.rs1]
            imm = self.rs2orimm
            return ['I', listaFetch[1], self.rd, rs1, imm] 

        if (self.type == 'B'):
            self.rs1 = listaFetch[2]
            self.rs2 = listaFetch[3]
            self.rs2orimm = listaFetch[4]
            rs1 = Registers.value_regs[self.rs1]
            rs2 = Registers.value_regs[self.rs2]
            imm = self.rs2orimm
            return ['B', listaFetch[1], rs1, rs2, imm]
        
    def runInstructionDecodeBinary(self, listafetch):
        a = 0

        
        

