import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from riscv_data.registers import Registers
from pipeline.RunPipeline import RunPipeline
from PyQt5.QtGui import QColor

YB = 60 #Altura dos Botoes
YT = 130 #Altura Tabelas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RISC-V Simulator")
        self.setGeometry(0, 0, 1366, 768)
        self.setFixedSize(1366, 768)
        self.setWindowIcon(QIcon("source/tomate.png"))

        self.regs = Registers()
        self.steps = ["Ifetch", "Reg/Dec", "Exec", "Mem", "WrB"]

        #self.instructions = ["lw", "sw", "sub", "lw", "add", "nop", "lw"] 
        self.file_name = None
        self.instructions = [] #Lista que contem as strings com o comando de cada instrucao, sem considerar label


        # self.main_memory = MainMemory()
        # self.mem = self.main_memory.memory
        self.run = False

        #botao de run (Roda todo pipeline)
        self.run_button = QPushButton("Run", self)
        self.initRun()

        #Botao de Next (Vai para proxima instrucao, ciclo por ciclo)
        self.next_button = QPushButton("Next", self)
        self.initNext()

        #Botao de Procurar Arquivos
        self.browse_button = QPushButton("Open File", self)
        self.initBrowse()
        
        #Endereco do Arquivo 
        self.file_path = QLineEdit(self)
        self.initFilePath()
        
        #Tabela Pipeline
        self.table_pipeline = QTableWidget(self)
        self.table_pipeline.setHorizontalHeaderLabels([""] * (2**10))

        self.initTablePipeline()
        
        #Tabela Registradores
        self.table_regs = QTableWidget(self)
        self.initTableRegs()

        #Tabela Memoria
        self.table_mem = QTableWidget(self)
        self.initTableMem()

        self.updateRunning()

    #----------------------------init--------------------
    def initRun(self):
        self.run_button.setGeometry(1366-240-200-40 ,YB,120,40)
        self.run_button.clicked.connect(self.runClicked)


    def initNext(self):
        self.next_button.setGeometry(1366-120-200,YB,120,40)
        self.next_button.clicked.connect(self.nextClicked)


    def initBrowse(self):
        self.browse_button.setGeometry(200,YB,120,40)
        self.browse_button.clicked.connect(self.browseClicked)


    def initFilePath(self):
        self.file_path.setGeometry(200 + 120 + 40, YB, 480, 40)
        self.file_path.setPlaceholderText("No File Selected")
        self.file_path.setReadOnly(True)

    def initTablePipeline(self):
        self.table_pipeline.setGeometry(483,YT,840,600)
        
        num_ciclos = num_ciclos = len(self.instructions) + 4 #numero de ciclos

        #seta o tamanho de linhas e colunas
        self.table_pipeline.setColumnCount(num_ciclos)
        self.table_pipeline.setRowCount(len(self.instructions))  
        
        self.table_pipeline.setVerticalHeaderLabels(self.instructions) #coloca o nome das instrucoes do lado   


    def initTableRegs(self):
        self.table_regs.setGeometry(43,YT,155,600)
        self.table_regs.setColumnCount(1)
        self.table_regs.setRowCount(32)
        self.table_regs.setHorizontalHeaderLabels(["Registers Values:"])
        
        chaves = list(self.regs.registers.keys()) #pega as chaves do dicionario de regs
        regs_labels = [f"{chaves[i]}" for i in range(32)]
        self.table_regs.setVerticalHeaderLabels(regs_labels)

    
    def initTableMem(self):
        self.table_mem.setGeometry(43+155+70,YT,150,600)
        self.table_mem.setColumnCount(1)
        self.table_mem.setRowCount(1000)
        self.table_mem.setHorizontalHeaderLabels(["Mem Content: "])
        

    #--------------------------------Clicked

    def browseClicked(self):
        #print("browsing file...")
        file = QFileDialog.getOpenFileName(self,'Select File', os.path.dirname(os.path.abspath(sys.argv[0])), "Supported Files (*.asm *.bin *.txt);;All Files (*.*)") 
        
        self.file_name = file[0]
        self.file_path.setPlaceholderText(self.file_name) #nome do arquivo é file[0]
        if self.file_name:  
            # Cria o pipeline mas NÃO roda nada ainda
            self.pipeline = RunPipeline(self.file_name)
            self.next_button.setEnabled(True)
            self.run_button.setEnabled(True)
            self.instructions = self.pipeline.listaInstrucoes
            self.total_cycles = len(self.instructions) + len(self.steps) - 1
            self.current_cycle = 0
            self.updatePipelineTable()

    def runClicked(self):
        if self.file_name:
            self.run_button.setDisabled(True)
            self.run = True
            
            # Executa pipeline e converte nomes
            self.pipeline = RunPipeline(self.file_name)

            self.pipeline.run()

            # Pega TODAS as instruções formatadas
            #self.instructions = self.pipeline.converteNome()
            self.instructions = self.pipeline.listaInstrucoes

            # Atualiza a tabela com essas instruções
            self.updatePipelineTable()

            self.updateRunning()
        else:
            print("SELECIONE UM ARQUIVO PARA EXECUTAR")




    def nextClicked(self):
        #print("next...")

        if self.file_name:
            # Executa apenas UMA instrução
            self.pipeline.next()
            self.current_cycle += 1

            # Atualiza registradores
            for i in range(32):
                self.table_regs.setItem(i, 0, QTableWidgetItem(str(self.pipeline.value_regs[i])))

            # Atualiza memória (só posições com valor)
            for i, val in enumerate(self.pipeline.memory):
                if val is not None:
                    self.table_mem.setItem(i, 0, QTableWidgetItem(str(val)))

            # Atualiza lista de instruções já executadas
            self.instructions = self.pipeline.listaInstrucoes
            self.updatePipelineTable()

            for i, val in enumerate(self.pipeline.memory):
                if val is not None:
                    self.table_mem.setItem(i, 0, QTableWidgetItem(str(val)))


            self.updateCycle()
            self.updateMemoryTable()
            #if self.pipeline.pc == -1:
                #print("Execução concluída!")
                #self.next_button.setDisabled(True)
        else:
            print("SELECIONE UM ARQUIVO PARA EXECUTAR")
 


    #------------------------Update
    def updateCycle(self):
        for i in range(len(self.instructions)):
            for j, step in enumerate(self.steps):
                col = i + j + 1  # +1 porque colunas começam em 1
                if col == self.current_cycle:
                    # Preenche a célula da instrução i no ciclo atual
                    self.table_pipeline.setItem(i, col - 1, QTableWidgetItem(step))

                    # Colore de acordo com o estágio
                    if step == "Ifetch":
                        self.table_pipeline.item(i, col - 1).setBackground(QColor(112, 214, 255))
                    elif step == "Reg/Dec":
                        self.table_pipeline.item(i, col - 1).setBackground(QColor(255, 112, 166))
                    elif step == "Exec":
                        self.table_pipeline.item(i, col - 1).setBackground(QColor(255, 151, 112))
                    elif step == "Mem":
                        self.table_pipeline.item(i, col - 1).setBackground(QColor(255, 214, 112))
                    elif step == "WrB":
                        self.table_pipeline.item(i, col - 1).setBackground(QColor(233, 255, 112))
                

    def updateMemoryTable(self):
        self.table_mem.clearContents()  # limpa antes de preencher
        for i, val in enumerate(self.pipeline.memory):
            if val is not None:
                self.table_mem.setItem(i, 0, QTableWidgetItem(str(val)))


    def updateRunning(self):
        if (self.run):
            #Tabela de Registradores Atualizada com o RUN:
            for i in range (0,32):
                self.table_regs.setItem(i,0, QTableWidgetItem(str(self.pipeline.value_regs[i])))
            #Preenchendo a Tabela com as instrucoes 

            for i in range (0,len(self.instructions)): #preenche com os steps
                    for j in range (0,5):
                        self.table_pipeline.setItem(i,j+i, QTableWidgetItem(self.steps[j]))
                        if (self.steps[j] == "Ifetch"): #["Ifetch", "Reg/Dec", "Exec", "Mem", "WrB"]
                            self.table_pipeline.item(i,j+i).setBackground(QColor(112, 214, 255))
                        elif self.steps[j] == "Reg/Dec":
                            self.table_pipeline.item(i,j+i).setBackground(QColor(255, 112, 166))
                        elif self.steps[j] == "Exec":
                            self.table_pipeline.item(i,j+i).setBackground(QColor(255, 151, 112))
                        elif self.steps[j] == "Mem":
                            self.table_pipeline.item(i,j+i).setBackground(QColor(255, 214, 112))
                        elif self.steps[j] == "WrB":
                            self.table_pipeline.item(i,j+i).setBackground(QColor(233, 255, 112))
            #self.table_pipeline.resizeColumnsToContents() #deixa com o tam do nome da etapa
            for i, val in enumerate(self.pipeline.memory):
                if val is not None:
                    self.table_mem.setItem(i, 0, QTableWidgetItem(str(val)))

    def updatePipelineTable(self):
        num_instrucoes = len(self.instructions)
        num_ciclos = num_instrucoes + 4 

        self.table_pipeline.setRowCount(num_instrucoes)
        self.table_pipeline.setColumnCount(num_ciclos)

        # Atualiza a coluna lateral com os nomes legíveis
        self.table_pipeline.setVerticalHeaderLabels(self.instructions)


'''
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
'''