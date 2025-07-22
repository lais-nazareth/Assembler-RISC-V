from RunPipeline import RunPipeline
    
    
class MemoryAcess:
    def __init__(self, list_execute):
        self.runPipeline = RunPipeline()
        self.memory = self.runPipeline.
        self.listaDecode = list_execute
        #[tipo, mnemonico, adress(rd), posicao a ler]
    def runMemorryAcess(self): #
        if (self.listaDecode[1] == "lw"):
            self.memory[self.listaDecode[2]] =  
        #elif(self.lista[1] == "sw"):
