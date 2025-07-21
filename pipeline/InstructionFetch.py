from riscv_data.instructions import Instructions
from riscv_data.registers import Registers
from utils import converteBin
#from Interface.interface import MainWindow


class InstructionFetch:
    def __init__(self, binaryfile: str = None, asmfile: str = None):
        self.binaryfile = binaryfile
        self.asmfile = asmfile
        self.currentline = None
        self.labels = {}
        if self.binaryfile:
            fp = open(self.binaryfile, "r")
            self.filelist = fp.readlines()
        else:
            self.findlabelsASM()
            fp = open(self.asmfile, "r")
            self.filelist = fp.readlines()

    def findlabelsASM(self):
        fp = open(self.asmfile, "r")
        filelist = fp.readlines()

        for i in range(len(filelist)):
            line = filelist[i].split()
            if len(line) > 0:
                if line[0][-1] == ':':
                    self.labels[line[0]] = i


        fp.close()


    def runInstructionFetch(self, pc):
        if self.binaryfile:
            return self.runInstructionFetchBinary(pc)
        else:
            return self.runInstructionFetchASM(pc)

        

    def runInstructionFetchASM(self, pc): # to do: fix imm for labels -> return label line as immediate
        """Le a linha no PC atual e retorna uma lista com os elementos da instrução

        Params:
            self
        
        Retorna:
        List
        lista com os elementos para o InstructionDecode entender a instrução:
        list[0] -> tipo
        list[1] -> mnemonico
        list[2:] -> resto da informação, dependendo da instrução

        """

        if len(self.filelist) == pc:
            return "FIM DA EXECUCAO"

        line = self.filelist[pc].split()
        self.currentline = line
        pc += 1

        if len(line) == 0:
            return self.runInstructionFetchASM(pc)
            

        if line[0] in self.labels:
            if len(line) == 1:
                return self.runInstructionFetchASM(pc)
            else:
                line = line[1:]

        
        instruction = Instructions.instructions[line[0]]
        print(instruction)

        if line[0] == "nop":
            return None

        if instruction["type"] == 'R': 
            rd = Registers.registers[line[1].rstrip(",")]
            rs1 = Registers.registers[line[2].rstrip(",")]
            rs2 = Registers.registers[line[3]]
            return ['R', line[0], rd, rs1, rs2], pc
        
        if instruction["type"] == "I": 
            if line[0] == "addi": # addi t0, t1, 40
                rd = Registers.registers[line[1].rstrip(",")]
                rs1 = Registers.registers[line[2].rstrip(",")]
                imm = Registers.registers[line[3]]
                return ['I', line[0], rd, rs1, imm], pc
            
            if line[0] == "lw": #lw t0, 40(t1)
                rd = Registers.registers[line[1].rstrip(",")]
                dec = line[2].split("(")
                imm = dec[0]
                rs1 = Registers.registers[dec[1].rstrip(")")]
                return ['I', line[0], rd, rs1, imm], pc
            
            if line[0] == "jalr": # jalr x1, 30(x2) ou jalr x1, label # UNFINISHED
                rd = Registers.registers[line[1].rstrip(",")]

                try:
                    dec = line[2].split("(")
                    imm = dec[0]
                    rs1 = Registers.registers[dec[1].rstrip(")")]
                    return ['I', line[0], rd, rs1, imm], pc
                except:
                    imm = self.labels[line[2]+':'] # fix label
                    return ['I', line[0], rd, imm], pc
            
        if instruction["type"] == "S": # sw t0, 40(t1)
                rd = Registers.registers[line[1].rstrip(",")]
                dec = line[2].split("(")
                imm = dec[0]
                rs1 = Registers.registers[dec[1].rstrip(")")]
                return ['I', line[0], rd, rs1, imm], pc
        
        if instruction["type"] == "J":
            if line[0] == "jal": # jal x1, offset ou jal x1, label
                rd = Registers.registers[line[1].rstrip(",")]
                try:
                    eval(line[2])
                    imm = line[2]
                except:
                    imm = self.labels[line[2]+':'] # fix label
                return ['J', line[0], rd, imm], pc
            
            if line[0] == "j":
                rd = 0
                try:
                    eval(line[1])
                    imm = line[1]
                except:
                    imm = self.labels[line[1]+':'] # fix label
                return ['J', line[0], rd, imm], pc
            
        if instruction["type"] == "B":
            rs1 = Registers.registers[line[1].rstrip(",")]
            rs2 = Registers.registers[line[2].rstrip(",")]
            try:
                eval(line[3])
                imm = line[3]
            except:
                imm = self.labels[line[3]+':'] # fix label
            return ['B', line[0], rs1, rs2, imm], pc


    def runInstructionFetchBinary(self, pc):
        # faz instruction fetch
        def tipoR(instrucao):
            funct7 = instrucao[0:7]
            rs2 = int(instrucao[7:12],2)
            rs1 = int(instrucao[12: 17],2)
            funct3 = instrucao[17:20]
            rd = int(instrucao[20:25],2)

            nome = None

            if funct3 == "000":
                if funct7 == "0000000":
                    nome = "add"
                elif funct7 == "0100000":
                    nome = "sub"
                elif funct7 == "0000001":
                    nome = "mul"
            elif funct3 == "111" and funct7 == "0000000":
                nome = "and"
            elif funct3 == "110" and funct7 == "0000000":
                nome = "or"
            elif funct3 == "100" and funct7 == "0000000":
                nome = "xor"
            elif funct3 == "100" and funct7 == "0000001":
                nome = "div"
            elif funct3 == "110" and funct7 == "0000001":
                nome = "rem"
            elif funct3 == "001" and funct7 == "0000000":
                nome = "sll"
            elif funct3 == "101" and funct7 == "0000000":
                nome = "srl"

            if nome is None:
                return "Instrução R-type não identificada"

            return ['R',nome, Registers.registers[rd], Registers.registers[rs1], Registers.registers[rs2]]
            
        def tipoI(instrucao):
            imm = instrucao[0:12]
            rs1 = int(instrucao[12:17],2)
            funct3 = instrucao[17:20]
            rd = int(instrucao[20:25],2)
            opcode = instrucao[25:32]

            # caso seja negativo em complemento de dois
            # trata sinal (12 bits com sinal)
            imm_val = int(imm,2)
            if imm[0] == '1':
                imm_val -= (1 << 12)

            nome = None

            if opcode == "0010011":
                if rd == 0 and rs1 == 0 and imm_val == 0:
                    return "nop"
                nome = "addi"

            elif opcode == "0000011":
                nome = "lw"

            elif opcode == "1100111":
                    nome = "jalr"
            else:
                return "Instrução do tipo-I não identificada"

            return ['I', nome, Registers.registers[rd], Registers.registers[rs1], imm] 

        def tipoS(instrucao):
            imm_11_5 = instrucao[0:7]
            rs2 = int(instrucao[7: 12],2)
            rs1 = int(instrucao[12:17],2)
            funct3 = instrucao[17:20]
            imm_4_0 = instrucao[20:25]

            #juntando e analisando o sinal do imediato
            imm = imm_11_5 + imm_4_0
            if imm[0] == '1':
                imm_val = int(imm, 2) - (1 << 12)
            else:
                imm_val = int(imm, 2)

            if funct3 == "010":
                nome = "sw"
            else:
                return "Instrução tipo-S desconhecida"

            return ['S', nome, Registers.registers[rd], Registers.registers[rs1], imm]

        def tipoB(instrucao):
            imm_12 = instrucao[0]
            imm_10_5 = instrucao[1:7]
            rs2 = int(instrucao[7:12],2)
            rs1 = int(instrucao[12:17],2)
            funct3 = instrucao[17:20]
            imm_4_1 = instrucao[20:24]
            imm_11 = instrucao[24]

            # Monta o imediato
            imm = imm_12 + imm_11 + imm_10_5 + imm_4_1 + "0"
            imm_val = int(imm, 2)
            if imm[0] == '1':
                imm_val -= (1 << 13)

            nome = None
            if funct3 == "000":
                nome = "beq"
            elif funct3 == "001":
                nome = "bne"
            elif funct3 == "100":
                nome = "blt"
            elif funct3 == "101":
                nome = "bge"

            if nome is None:
                return "Instrução tipo-B desconhecida"

            return ['B', nome,  Registers.registers[rs1], Registers.registers[rs2], imm_val]
            
        def tipoJ(instrucao):
            imm_20 = instrucao[0:20]
            imm_10_1 = instrucao[1:11]
            imm_11 = instrucao[11]
            imm_19_12 = instrucao[12:20]
            rd = int(instrucao[20:25],2)

            imm = imm_20 + imm_19_12 + imm_11 + imm_10_1 + "0"
            imm_val = int(imm, 2)
            if imm[0] == '1':
                imm_val -= (1 << 21)

            if rd == 0:
                return ['J', 'j', imm_val]
            else:
                return ['J', "jal", Registers.registers[rd], imm_val]
                
        def decodifica(instrucao):
            opcode = instrucao[25:32]

            if opcode == "0110011":
                instr_formatada = tipoR(instrucao)

            elif opcode in ("0010011", "0000011", "1100111"):
                instr_formatada = tipoI(instrucao)

            elif opcode == "0100011":
                instr_formatada = tipoS(instrucao)

            elif opcode == "1100011":
                instr_formatada = tipoB(instrucao)

            elif opcode == "1101111":
                instr_formatada = tipoJ(instrucao)

            else:
                print("Opcode não suportado")

            return instr_formatada
            