from riscv_data.instructions import Instructions
from riscv_data.registers import Registers
from utils import converteBin

class InstructionFetch:
    def instructionFetch(self, line, PC):

        instruction = Instructions.instructions[line[0]]
        tipo = instruction["type"]

        match tipo:
            case "R": # func7 / rs2 / rs1 / funct3 / rd / opcode
                bitstring = instruction["func7"] + converteBin(Registers.registers[line[3]], 5) + converteBin(Registers.registers[line[2]], 5) + instruction["func3"] + converteBin(Registers.registers[line[1]], 5) + instruction["opcode"]
                PC = self.incrementPC(PC)
            case "I": # imm[11:0] / rs1 / funct3 / rd / opcode 
                if instruction[0] == "l":
                    imm, reg = self.storeLoadInterpreting(line)
                    bitstring = converteBin(imm, 12) + converteBin(Registers.registers[reg]) + instruction["func3"] + converteBin(Registers.registers[line[1]], 5) + instruction["opcode"]
                else:
                    bitstring = converteBin([line[3]], 12) + converteBin(Registers.registers[line[2]], 5) + instruction["func3"] + converteBin(Registers.registers[line[1]], 5) + instruction["opcode"]
                PC = self.incrementPC(PC)
            case "S": # imm[11:5] / rs2 / rs1 / funct3 / imm[4:0] / opcode 
                imm, reg = InstructionFetch.storeLoadInterpreting(line)
                imm = converteBin(imm, 12)
                immSplit1 = imm[0:6]
                immSplit2 = imm[6:]
                bitstring = immSplit1 + converteBin(Registers.registers[reg], 5) + converteBin(Registers.registers[line[1]], 5) + instruction["func3"] + immSplit2 + instruction["opcode"]
                PC = self.incrementPC(PC)
                
            case "B": # imm[12|10:5] / rs2 / rs1 / funct3 / imm[4:1|11] / opcode
                rotulo = line[3]
                
                imm = self.calcularImediato(PC, rotulo)
                imm1 = "" # implementar
                imm2 = ""

                bitstring = imm1 + converteBin(Registers.registers[line[2]], 5) + converteBin(Registers.registers[line[1]], 5) + instruction["func3"] + imm2 + instruction["opcode"]


            case "U": # imm[31:12] / rd / opcode
                imm = converteBin(eval(line[2]), 20)
                bitstring = imm + converteBin(Registers.registers[line[1]], 5) + instruction["opcode"]

            case "J": #imm[20|10:1|11|19:12] / rd / opcode
                imm = ""#
        
        InstructionFetch.incrementPC()

    def incrementPC(PC):
        return PC+4
    
    def storeLoadInterpreting(self, line):
        s = line[2]

        sStrip = s.rstrip(")")
        parts = sStrip.split("(")
        imm = parts[0]
        reg = parts[1]
        return imm, reg
    
    def calcularImediato(PC, rotulo):
        a=0
        # implementar