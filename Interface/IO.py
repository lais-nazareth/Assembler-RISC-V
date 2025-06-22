import sys
from PyQt5.QtWidgets import (QFileDialog)

class IO:
    @staticmethod
    def fileOpen(textEdit):
        file = QFileDialog.getOpenFileName(textEdit,'Select File', 'D:/uff-codigos/3-Semestre/ArquiteturaDeComputadores/riscv', 'ASM File (*.asm)')
        if file[0]:  
            f = open(file[0], "r")
            linha = f.read()
            textEdit.setPlainText(linha)

    #cria janela pra escrever o nome do arquivo
    #def newFile(self):

    #@staticmethod
    #def saveFile():
