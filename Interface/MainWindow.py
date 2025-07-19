import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from pipeline.RunPipeline import *

Y = 120 #Altura dos Botoes

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RISC-V Simulator")
        self.setGeometry(0, 0, 1366, 768)
        self.setFixedSize(1366, 768)
        self.setWindowIcon(QIcon("Interface/source/tomate.png"))
        self.file = None
        
        
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
    
    
    def initRun(self):
        self.run_button.setGeometry(1366-240-200-40 ,Y,120,40)
        self.run_button.clicked.connect(self.runClicked)


    def runClicked(self):
        if self.file:
            print("running...");
            self.run_button.setDisabled(True) #Ajustar para quando terminar de rodar voltar a ser false:
            RunPipeline(self.file[0])
        else:
            print("SELECIONE UM ARQUIVO PARA EXECUTAR")
        #A Implementar...


    def initNext(self):
        self.next_button.setGeometry(1366-120-200,Y,120,40)
        self.next_button.clicked.connect(self.nextClicked)


    def nextClicked(self):
        print("next...")
        #A Implementar...


    def initBrowse(self):
        self.browse_button.setGeometry(200,Y,120,40)
        self.browse_button.clicked.connect(self.browseClicked)


    def browseClicked(self):
        #print("browsing file...")
        self.file = QFileDialog.getOpenFileName(self,'Select File', 'C:/', 'BIN File (*.bin)')
        self.file_path.setPlaceholderText(self.file[0]) #nome do arquivo é file[0]
        
    

    def initFilePath(self):
        self.file_path.setGeometry(200 + 120 + 40, Y, 480, 40)
        self.file_path.setPlaceholderText("No File Selected")
        self.file_path.setReadOnly(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()