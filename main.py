import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from riscv_data.registers import Registers



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
        self.instructions = ["lw", "sw", "sub", "lw", "add", "nop", "lw"] 

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
        self.initTablePipeline()
        
        #Tabela Registradores
        self.table_regs = QTableWidget(self)
        self.initTableRegs()

        #Tabela Memoria
        self.table_mem = QTableWidget(self)
        self.initTableMem()

        self.updateRunning()


    def initRun(self):
        self.run_button.setGeometry(1366-240-200-40 ,YB,120,40)
        self.run_button.clicked.connect(self.runClicked)


    def runClicked(self):
        #print("running...");
        self.run_button.setDisabled(True) #Ajustar para quando terminar de rodar voltar a ser false
        self.run = True
        self.updateRunning()



    def initNext(self):
        self.next_button.setGeometry(1366-120-200,YB,120,40)
        self.next_button.clicked.connect(self.nextClicked)


    def nextClicked(self):
        print("next...")
        #A Implementar...


    def initBrowse(self):
        self.browse_button.setGeometry(200,YB,120,40)
        self.browse_button.clicked.connect(self.browseClicked)


    def browseClicked(self):
        #print("browsing file...")
        file = QFileDialog.getOpenFileName(self,'Select File', 'C:/', 'BIN File (*.bin)')
        self.file_path.setPlaceholderText(file[0]) #nome do arquivo é file[0]
    

    def initFilePath(self):
        self.file_path.setGeometry(200 + 120 + 40, YB, 480, 40)
        self.file_path.setPlaceholderText("No File Selected")
        self.file_path.setReadOnly(True)


    def initTablePipeline(self):
        self.table_pipeline.setGeometry(483,YT,840,600)
        
        num_ciclos = len(self.instructions) + 4 #numero de ciclos

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
        

    def updateRunning(self):
        if (self.run):
            #Tabela de Registradores Atualizada com o RUN:
            for i in range (0,32):
                self.table_regs.setItem(i,0, QTableWidgetItem(str(self.regs.value_regs[i])))
            #Preenchendo a Tabela com as instrucoes 
            for i in range (0,len(self.instructions)): #preenche com os steps
                    for j in range (0,5):
                        self.table_pipeline.setItem(i,j+i, QTableWidgetItem(self.steps[j]))
            #self.table_pipeline.resizeColumnsToContents() #deixa com o tam do nome da etapa


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()