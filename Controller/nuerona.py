import imp
from operator import mod
from PySide2.QtWidgets import QWidget,QApplication,QMessageBox
from Views.Main import MainWindow
from Views.PesoFinal import PesoFinals

from PySide2.QtCore import Qt


from cProfile import label
from turtle import color
import numpy as np 
import math
from matplotlib import colors
import matplotlib.pyplot as plt



class Neurona(QWidget,MainWindow,PesoFinals):
      
      def __init__(self,parent=None):
            super().__init__(parent)
            self.setupUi(self)
            self.matrizX = []
            self.matrizY = []
            self.guardarDato = []
            self.grafica1 = []
            self.grafica2 = []
            self.grafica3 = []
            self.grafica4 = []
            self.grafica5 = []
            self.PesosFinal = []
            self.pushButtonIniciar.clicked.connect(self.Start)
            self.setWindowTitle("Hola mundo")
            
      def CargarDatos(self):
                        
            vectorX = []
            vectorY = []
            enteroX = []
            with open("matriz.txt") as f:
                  linea = f.readlines()
            i = 0
            while i < len(linea):
                  lin = linea[i].replace("X","")
                  lin = lin.replace("Y","")
                  lin = lin.replace("=","")
                  lin = lin.replace("[","")
                  lin = lin.replace("]","")
                  lin = lin.replace("\n","")
                  lin = lin.split(";")
                  self.guardarDato.append(lin)
                  i = i + 1
            
            matriz = self.guardarDato[0]
            vector = self.guardarDato[1]
            splitY = "".join(vector).split(",")                
      
 
            for i in range(len(matriz)):
                  x = matriz[i]
                  valor = "".join(x).split(",")
                  num = valor
                  vectorX.append(num)
            
            
            for i in range(len(splitY)):
                  convertirY = int(splitY[i])
                  vectorY.append(convertirY)
      
            columna = len(vectorX)                  
            fila = len(vectorX[0])
            vectorMatriz = np.array(vectorX).reshape(columna,fila)
            matrizEnetro = vectorMatriz.astype(int)
        
            self.matrizX = np.array(matrizEnetro)
            self.matrizY = np.array(vectorY)  
            return self.matrizX,self.matrizY
            
      def PesoVacio(self,matriz):
            tamX = len(matriz[0])
            pesos = [np.random.uniform(-1,1) for i in range(tamX)]
            w = np.array(pesos)
            return w

      def U(self,peso,matrizX):
            x = matrizX
            w = peso
            u = np.dot(x,w)
            return u

      def Ufinal(self,peso,matrizX):
            x = matrizX
            w = peso
            uFinal = np.dot(x,w)
            return uFinal

      def Yc(self,peso,matrizX):
            u = self.U(peso,matrizX)
            yc = []
            for x in range(len(u)):
                  if u[x] <= 0:
                        yc.append(0)
                  elif u[x] > 0:
                        yc.append(1)
            return yc

      def YcComprobar(self,producto):
            u = producto
            yc = []
            for x in range(len(u)):
                  if u[x] <= 0:
                        yc.append(0)
                  elif u[x] > 0:
                        yc.append(1)
            return yc

      def Error(self,peso,matrizX,matrizY):
            yc = self.Yc(peso,matrizX)
            y = matrizY
            resta = yc - y
            error = np.array(resta)
            return error

      def Norma(self,peso,matrizX,matrizY):
            error = self.Error(peso,matrizX,matrizY)
            norma = np.linalg.norm(error)
            return norma

      def NeuronaStart(self,tasa,umbral,peso,matrizX,matrizY,id):
            ward = []
            w = peso
            bandera = False
            while bandera == False:
                  error = self.Error(w,matrizX,matrizY)
                  norma = self.Norma(w,matrizX,matrizY)
                  x = matrizX
                  tasa = tasa
                  xe = np.dot(error,x)
                  tasaXe = np.dot(tasa,xe)
                  w = w - tasaXe
                  ward = w
                  if id == 1:
                        self.grafica1.append(norma)
                  elif id == 2:
                        self.grafica2.append(norma)
                  elif id == 3:
                        self.grafica3.append(norma)
                  elif id == 4:
                        self.grafica4.append(norma)
                  elif id == 5:
                        self.grafica5.append(norma)
                  if norma < umbral:
                        bandera = True
                  else:
                        bandera = False
            
            print( "ward-->",ward)
            otroU = self.Ufinal(ward,matrizX)
            print(otroU,"<-<-otroU" )
            ycOtro = self.YcComprobar(otroU)
            print(ycOtro," <-COMPROBAR\n------****----")
            print("Peso final: ",ward,"\n-----****----",id)
            self.PesosFinal.append(ward)
            print(self.PesosFinal,"<- en antes graficar")
            self.Graficar(ward)
            return ward

      def Graficar(self,pesosFinal):
            plt.plot(self.grafica1,label = "Grafica 1",color = "Blue")
            plt.plot(self.grafica2,label = "Grafica 2",color = "Red")
            plt.plot(self.grafica3,label = "Grafica 3",color = "Navy")
            plt.plot(self.grafica4,label = "Grafica 4",color = "Purple")
            plt.plot(self.grafica5,label = "Grafica 5",color = "Fuchsia")
            plt.legend()
            plt.show()
       
            
    
            
      def Start(self):
            modulo = Neurona()
            matrizX,matrizY=modulo.CargarDatos()
            ent = []

            if self.lineEditPesos.text() == "":
                  w = np.array(self.PesoVacio(matrizX))
            else:
                  peso =self.lineEditPesos.text().split(",")
                  for i in range(len(peso)):
                        lst = peso[i]
                        st = "".join(lst)
                        guardar = float(st)
                        ent.append(guardar)
                  w = np.array(ent)
                  
            tasa = float(self.lineEditTasa.text())
            umbral = float(self.lineEditUmbral.text())
            print("1")
            pesoFinal1 = modulo.NeuronaStart(tasa,umbral,w,matrizX,matrizY,id=1)
            ent.clear()
            

                  
            if self.lineEditPesos2.text() == "":
                  w2 = np.array(self.PesoVacio(matrizX))
            else:
                  peso2 =self.lineEditPesos2.text().split(",")
                  for i in range(len(peso2)):
                        lst = peso2[i]
                        st = "".join(lst)
                        guardar = float(st)
                        ent.append(guardar)
                  w2 = np.array(ent)
            tasa2 = float(self.lineEditTasa2.text())
            umbral2 = float(self.lineEditUmbral2.text())
            print("2")
            modulo = Neurona()
            modulo.CargarDatos()
            pesoFinal2 = modulo.NeuronaStart(tasa2,umbral2,w2,matrizX,matrizY,id=2)
            ent.clear()
            
            if self.lineEditPeso3.text() == "":
                  w3 = np.array(self.PesoVacio(matrizX))
            else:
                  peso3 =self.lineEditPeso3.text().split(",")
                  for i in range(len(peso3)):
                        lst = peso3[i]
                        st = "".join(lst)
                        guardar = float(st)
                        ent.append(guardar)
                  w3 = np.array(ent)
            tasa3 = float(self.lineEditTasa3.text())
            umbral3 = float(self.lineEditUmbral3.text())
            modulo = Neurona()
            modulo.CargarDatos()
            pesoFinal3 = modulo.NeuronaStart(tasa3,umbral3,w3,matrizX,matrizY,id=3)
            ent.clear()
            
            if self.lineEditPeso4.text() == "":
                  w4 = np.array(self.PesoVacio(matrizX))
            else:
                  peso4 =self.lineEditPeso4.text().split(",")
                  for i in range(len(peso4)):
                        lst = peso4[i]
                        st = "".join(lst)
                        guardar = float(st)
                        ent.append(guardar)
                  w4 = np.array(ent)
            tasa4 = float(self.lineEditTasa4.text())
            umbral4 = float(self.lineEditUmbral4.text())
            modulo = Neurona()
            modulo.CargarDatos()
            pesoFinal4 = modulo.NeuronaStart(tasa4,umbral4,w4,matrizX,matrizY,id=4)
            ent.clear()
            
            if self.lineEditPeso5.text() == "":
                  w5 = np.array(self.PesoVacio(matrizX))
            else:
                  peso5 =self.lineEditPeso5.text().split(",")
                  for i in range(len(peso5)):
                        lst = peso5[i]
                        st = "".join(lst)
                        guardar = float(st)
                        ent.append(guardar)
                  w5 = np.array(ent)
            tasa5 = float(self.lineEditTasa5.text())
            umbral5 = float(self.lineEditUmbral5.text())
            modulo = Neurona()
            modulo.CargarDatos()
            pesoFinal5 = modulo.NeuronaStart(tasa5,umbral5,w5,matrizX,matrizY,id=5)
            ent.clear()
            print(pesoFinal1,"\t",pesoFinal2,"\t",pesoFinal3,"\t",pesoFinal4,"\t",pesoFinal5)
            QMessageBox.about(self, "Peso final", f"El Peso final 1 ={pesoFinal1}\nEl Peso final 2 = {pesoFinal2}\nEl Peso final 3 = {pesoFinal3}\nEl Peso final 4 = {pesoFinal4}\nEl Peso final 5 = {pesoFinal5}\n")
            
            # QMessageBox.about(self,"XD","The document has been modified.")
            # QMessageBox.exec()
            

