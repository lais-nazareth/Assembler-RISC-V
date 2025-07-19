import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from pipeline.RunPipeline import RunPipeline
from Interface.interface import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()