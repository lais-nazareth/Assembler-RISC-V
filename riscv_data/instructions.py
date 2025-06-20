

class Instructions:
    instructions = {
        # tipo R
        "add": {"type": "R", "opcode": "0110011", "func3": "123", "func7": "1234567"}, 
        "sub": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
        "xor": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
        "or": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
        "and": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
        "sll": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
        "srl": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
        "sra": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
        "slt": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
        "sltu": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
            

        # tipo I
        "addi": {"type": "I", "opcode": "0010011", "func3": "", "func7": None},
        "xori": {"type": "I", "opcode": "0010011", "func3": "", "func7": None},
        "ori": {"type": "I", "opcode": "0010011", "func3": "", "func7": None},
        "andi": {"type": "I", "opcode": "0010011", "func3": "", "func7": None},
        "sltu": {"type": "I", "opcode": "0010011", "func3": "", "func7": ""}, 
        "slli": {"type": "I", "opcode": "0010011", "func3": "", "func7": ""}, 
        "srli": {"type": "I", "opcode": "0010011", "func3": "", "func7": ""}, 
        "srai ": {"type": "I", "opcode": "0010011", "func3": "", "func7": ""}, 
        "slti": {"type": "I", "opcode": "0010011", "func3": "", "func7": None},
        "sltiu": {"type": "I", "opcode": "0010011", "func3": "", "func7": None},
                #load
        "lb": {"type": "I", "opcode": "0010011", "func3": ""},
        "lh": {"type": "I", "opcode": "0010011", "func3": ""},
        "lw": {"type": "I", "opcode": "0010011", "func3": ""},
        "lbu": {"type": "I", "opcode": "0010011", "func3": ""},
        "lhu": {"type": "I", "opcode": "0010011", "func3": ""},


        # tipo S
        "sb": {"type": "S", "opcode": "0100011", "func3": "000", "func7": None}, 
        "sh": {"type": "S", "opcode": "0100011", "func3": "001", "func7": None}, 
        "sw": {"type": "S", "opcode": "0100011", "func3": "002", "func7": None},

        
        # tipo B 
        "beq": {"type": "B", "opcode": "1100011", "func3": "000", "func7": None},
        "bne": {"type": "B", "opcode": "1100011", "func3": "0011", "func7": None},
        "blt": {"type": "B", "opcode": "1100011", "func3": "100", "func7": None},
        "bge": {"type": "B", "opcode": "1100011", "func3": "101", "func7": None},
        "bltu": {"type": "B", "opcode": "1100011", "func3": "110", "func7": None},
        "bgeu": {"type": "B", "opcode": "1100011", "func3": "111", "func7": None},

        # tipo J
        "jal": {"type": "J", "opcode": "1101111", "func3": None, "func7": None},
        "jalr": {"type": "I", "opcode": "1100111", "func3": "000", "func7": None}, # tipo I mas funciona como jump

        # tipo U
        "lui": {"type": "U", "opcode": "0110111", "func3": None, "func7": None},
        "auipc": {"type": "U", "opcode": "0010111", "func3": None, "func7": None},

        # Syscalls
        "ecall": {"type": "I", "opcode": "1110011", "func3": "000", "func7": "000"},
        "ebreak": {"type": "I", "opcode": "1110011", "func3": "000", "func7": "001"},
        
        # Standard Extensions
            #TIPO R
            "mul": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
            "mulh": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
            "mulsu": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
            "mulu": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
            "div": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
            "divu": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
            "rem": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}, 
            "remu": {"type": "R", "opcode": "0110011", "func3": "0", "func7": "0"}
        }

