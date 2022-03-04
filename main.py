import imp
from PySide2.QtWidgets import QApplication
from Controller.nuerona import Neurona

if __name__ == '__main__':
      app = QApplication()
      window = Neurona()
      window.show()
      app.exec_()
    