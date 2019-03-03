from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from src.game import Game

if __name__ == '__main__':
    app = QApplication(argv)
    widget = Game()
    widget.show()
    exit(app.exec_())
