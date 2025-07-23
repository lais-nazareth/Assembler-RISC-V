class DeteccaoHazards:
    def __init__(self, forwarding_enabled=False, binaryfile: str = None, asmfile: str = None):
        self.forwarding_enabled = forwarding_enabled
        self.binaryfile = binaryfile
        self.asmfile = asmfile
        self.filelist = None

        if self.binaryfile:
            fp = open(self.binaryfile, "r")
            self.filelist = fp.readlines()
            
            self.detect(self.filelist)
            fp.close()

            with open(self.binaryfile, "r") as f:
                self.filelist = []
                for linha in f:
                    instrucao = linha.strip()
                    if len(instrucao) == 32:
                        self.filelist.append(instrucao)
        else:
            self.findlabelsASM()
            fp = open(self.asmfile, "r")
            self.filelist = fp.readlines()

    def detect(self, instr_atual, ex_instr, mem_instr, wb_instr):
        if not instr_atual or instr_atual[0] == 'B':
            return False  # ignorar branch por enquanto

        using_regs = []
        if instr_atual[0] == 'R':
            using_regs = [instr_atual[3], instr_atual[4]]
        elif instr_atual[0] == 'I':
            using_regs = [instr_atual[3]]
        elif instr_atual[0] == 'S':
            using_regs = [instr_atual[3]]
