
class MemoryAccess:
    def __init__(self):
        self.m = 0
        # listexecute: [tipo, mnemonico, valor(rd), posicao a ler]
    def runMemoryAccess(self, list_execute, memory): #
        if (list_execute[1] == "lw"):
            return memory[list_execute[3]] #retorna o valor que está no lw
        elif(list_execute[1] == "sw"):
            memory[list_execute[3]] = list_execute[2] # salva na posicao o valor de rd
    
