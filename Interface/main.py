import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QPushButton, QFormLayout, QMenuBar, QAction, QFileDialog)
from PyQt5.QtGui import (QIcon)

from IO import IO

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador de Montador RISC-V")
        #self.setGeometry(x,y,width, height)
        self.setGeometry(0, 0, 1366, 768)
        self.setWindowIcon(QIcon("Interface/pictures/tomate.png"))
        self.button = QPushButton("Run", self)
        

        self.createText()
        self.createMenu()
        self.initUI()
        

    
    def createText(self):
        layout = QFormLayout()
        self.setLayout(layout)
        self.textEdit = QTextEdit(self)
        layout.addRow(self.textEdit)
        self.textEdit.setGeometry(40, 40, 590, 688)
        self.textEdit.setStyleSheet("font-size : 16px; font-family: Arial")

    def createMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        helpMenu = mainMenu.addMenu("Help")
        
        openFile = QAction("Open", self)
        #openFile.setStatusTip('Open Editor')
        openFile.triggered.connect(lambda: IO.fileOpen(self.textEdit))

        saveFile = QAction("Save", self)
        saveFile.setShortcut("Ctrl+S")

        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)


    def initUI(self):
        self.button.setGeometry(250,738,100,20)
        self.button.clicked.connect(self.run)


    def run(self):
        print(self.textEdit.toPlainText())




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
