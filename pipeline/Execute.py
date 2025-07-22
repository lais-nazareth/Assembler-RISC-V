

class Execute():
    def __init__(self):
        self.type = None
        self.instruction = None

    def runExecute(self, listaDecode, pc):
        
        if listaDecode[0] == 'R': # formato listaDecode: [tipo, mnemonico, adress(rd), rs1, rs2]
            match listaDecode[1]:
                case 'add':
                    return ['R', listaDecode[1], listaDecode[2], listaDecode[3] + listaDecode[4]], pc
                case 'sub':
                    return ['R', listaDecode[1], listaDecode[2], listaDecode[3] - listaDecode[4]], pc
                case 'mul':
                    return ['R', listaDecode[1], listaDecode[2], listaDecode[3] * listaDecode[4]], pc
                case 'div':
                    return ['R', listaDecode[1], listaDecode[2], listaDecode[3] // listaDecode[4]], pc
                case 'rem':
                    return ['R', listaDecode[1], listaDecode[2], listaDecode[3] % listaDecode[4]], pc
                case 'xor':
                    return ['R', listaDecode[1], listaDecode[2], listaDecode[3] ^ listaDecode[4]], pc
                case 'and':
                    return ['R', listaDecode[1], listaDecode[2], listaDecode[3] and listaDecode[4]], pc
                case 'or':
                    return ['R', listaDecode[1], listaDecode[2], listaDecode[3] or listaDecode[4]], pc
                case 'sll':
                    return ['R', listaDecode[1], listaDecode[2], listaDecode[3] << listaDecode[4]], pc
                case 'srl':
                    return ['R', listaDecode[1], listaDecode[2], listaDecode[3] >> listaDecode[4]], pc
                
        if listaDecode[0] == 'I': # formato listaDecode: [tipo, mnemonico, adress(rd), rs1, imm]
            match listaDecode[1]:
                case 'addi':
                    return ['I', listaDecode[1], listaDecode[2], listaDecode[3] + listaDecode[4]], pc
                case 'lw':
                    return ['I', listaDecode[1], listaDecode[2], listaDecode[3] + listaDecode[4]], pc # retorna [tipo, mnemonico, adress(rd), posicao a ler]
                
        # if listaDecode[0] == 'J': # o valor imm vai pro PC | rd = PC+4 | PC += imm 
        #     return ['I', listaDecode[2], pc + listaDecode[3]], pc
        
        if listaDecode[0] == 'B':
            match listaDecode[1]:
                case 'beq':
                    if (listaDecode[2] == listaDecode[3]):
                        return ['B', listaDecode[1], (listaDecode[2] == listaDecode[3]), pc + listaDecode[4]], pc + listaDecode[4]
                    else:
                        return ['B', listaDecode[1], (listaDecode[2] == listaDecode[3]), pc + listaDecode[4]], pc 
                case 'bne':
                    if (listaDecode[2] != listaDecode[3]):
                        return ['B', listaDecode[1], (listaDecode[2] != listaDecode[3]), pc + listaDecode[4]], pc + listaDecode[4]
                    else:
                        return ['B', listaDecode[1], (listaDecode[2] != listaDecode[3]), pc + listaDecode[4]], pc
                case 'bge':
                    if (listaDecode[2] >= listaDecode[3]):
                        return ['B', listaDecode[1], (listaDecode[2] >= listaDecode[3]), pc + listaDecode[4]], pc + listaDecode[4]
                    else:
                        return ['B', listaDecode[1], (listaDecode[2] >= listaDecode[3]), pc + listaDecode[4]], pc
                case 'blt':
                    if (listaDecode[2] < listaDecode[3]):
                        return ['B', listaDecode[1], (listaDecode[2] < listaDecode[3]), pc + listaDecode[4]], pc + listaDecode[4]
                    else:
                        return ['B', listaDecode[1], listaDecode[1], (listaDecode[2] < listaDecode[3]), pc + listaDecode[4]], pc
                    
        if listaDecode[0] == 'J': # o valor imm vai pro PC | rd = PC+4 | PC += imm 
            match listaDecode[1]:
                case 'jal':
                    return ['J', listaDecode[1], listaDecode[2], pc + 1], pc + listaDecode[3]
                case 'J':
                    return ['J', listaDecode[1], listaDecode[2], 0], pc + listaDecode[3]
