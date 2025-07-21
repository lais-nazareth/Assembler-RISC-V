

class Execute():
    def __init__(self):
        self.type = None
        self.instruction = None

    def runExecute(self, listaDecode, pc):
        
        if listaDecode[0] == 'R': # formato listaDecode: [tipo, mnemonico, adress(rd), rs1, rs2]
            match listaDecode[1]:
                case 'add':
                    return ['R', listaDecode[2], listaDecode[3] + listaDecode[4]]
                case 'sub':
                    return ['R', listaDecode[2], listaDecode[3] - listaDecode[4]]
                case 'mul':
                    return ['R', listaDecode[2], listaDecode[3] * listaDecode[4]]
                case 'div':
                    return ['R', listaDecode[2], listaDecode[3] // listaDecode[4]]
                case 'rem':
                    return ['R', listaDecode[2], listaDecode[3] % listaDecode[4]]
                case 'xor':
                    return ['R', listaDecode[2], listaDecode[3] ^ listaDecode[4]]
                case 'and':
                    return ['R', listaDecode[2], listaDecode[3] and listaDecode[4]]
                case 'or':
                    return ['R', listaDecode[2], listaDecode[3] or listaDecode[4]]
                case 'sll':
                    return ['R', listaDecode[2], listaDecode[3] << listaDecode[4]]
                case 'srl':
                    return ['R', listaDecode[2], listaDecode[3] >> listaDecode[4]]
                
        if listaDecode[0] == 'I': # formato listaDecode: [tipo, mnemonico, adress(rd), rs1, imm]
            match listaDecode[1]:
                case 'addi':
                    return ['I', listaDecode[2], listaDecode[3] + listaDecode[4]]
                case 'lw':
                    return ['I', listaDecode[2], listaDecode[3] + listaDecode[4]]
                
        if listaDecode[0] == 'J': # o valor imm vai pro PC | rd = PC+4 | PC += imm 
            return ['I', listaDecode[2], pc + listaDecode[3]]
        
        if listaDecode[0] == 'B':
            match listaDecode[1]:
                case 'beq':
                    return ['B', (listaDecode[2] == listaDecode[3]), pc + listaDecode[4]]
                case 'bne':
                    return ['B', (listaDecode[2] != listaDecode[3]), pc + listaDecode[4]]
                case 'bge':
                    return ['B', (listaDecode[2] >= listaDecode[3]), pc + listaDecode[4]]
                case 'blt':
                    return ['B', (listaDecode[2] < listaDecode[3]), pc + listaDecode[4]]