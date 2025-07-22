
class Instructions:
    instructions = {
        # tipo R
        "add": {"type": "R", "opcode": "0110011", "func3": "000", "func7": "0000000"}, 
        "sub": {"type": "R", "opcode": "0110011", "func3": "000", "func7": "0100000"}, 
        "xor": {"type": "R", "opcode": "0110011", "func3": "100", "func7": "0000000"}, 
        "or": {"type": "R", "opcode": "0110011", "func3": "110", "func7": "0000000"}, 
        "and": {"type": "R", "opcode": "0110011", "func3": "111", "func7": "0000000"}, 
        "sll": {"type": "R", "opcode": "0110011", "func3": "001", "func7": "0000000"}, 
        "srl": {"type": "R", "opcode": "0110011", "func3": "101", "func7": "00000000"}, 
            

        # tipo I
        "addi": {"type": "I", "opcode": "0010011", "func3": "000", "func7": None},

        #load
        "lw": {"type": "I", "opcode": "0000011", "func3": "010", "func7": None},

        # tipo S
        "sw": {"type": "S", "opcode": "0100011", "func3": "010", "func7": None},

        
        # tipo B 
        "beq": {"type": "B", "opcode": "1100011", "func3": "000", "func7": None},
        "bne": {"type": "B", "opcode": "1100011", "func3": "001", "func7": None},
        "blt": {"type": "B", "opcode": "1100011", "func3": "100", "func7": None},
        "bge": {"type": "B", "opcode": "1100011", "func3": "101", "func7": None},

        # tipo J
        "j": {"type": "J", "opcode": "1101111", "func3": None, "func7": None},
        "jal": {"type": "J", "opcode": "1101111", "func3": None, "func7": None},
        "jalr": {"type": "I", "opcode": "1100111", "func3": "000", "func7": None}, # tipo I mas funciona como jump
        
        # Standard Extensions
        #TIPO R
        "mul": {"type": "R", "opcode": "0110011", "func3": "000", "func7": "0000001"}, 
        "div": {"type": "R", "opcode": "0110011", "func3": "100", "func7": "0000001"}, 
        "rem": {"type": "R", "opcode": "0110011", "func3":"110", "func7": "0000001"}
        }


