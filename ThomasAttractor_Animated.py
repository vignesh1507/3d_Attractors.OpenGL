import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtCore
import pyqtgraph.opengl as gl
import sys 

class Simulation(object):   
    def __init__(self, x, y, z, a, deltatime):    
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = gl.GLViewWidget() 
        self.window.setGeometry(480, 270, 800, 600) 
        self.window.setWindowTitle("Simulation")    
        self.window.setCameraPosition(distance=30, elevation=100) 
        self.window.show()

        self.x, self.y, self.z = x, y, z 
        self.a, self.deltatime = a, deltatime
        self.points_list = []  # create an empty list    

    #run algorithm and draw lines
    def Update(self):
        dx = (np.sin(self.y) - (self.a * self.x)) * self.deltatime
        dy = (np.sin(self.z) - (self.a * self.y)) * self.deltatime
        dz = (np.sin(self.x) - (self.a * self.z)) * self.deltatime
        self.x = self.x + dx
        self.y = self.y + dy
        self.z = self.z + dz
        newpoint = (self.x, self.y, self.z) 
        self.points_list.append(newpoint)  
        self.points = np.array(self.points_list) 
        self.draw()  

    def draw(self):
        try: self.window.removeItem(self.drawpoints)
        except Exception: pass
        self.drawpoints = gl.GLLinePlotItem(pos=self.points, width=1, antialias=True) 
        self.window.addItem(self.drawpoints) 
    
    #start properly
    def start(self):
        QtWidgets.QApplication.instance().exec_()

    #animate and update  
    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.Update)
        timer.start(20)
        self.start()

sim = Simulation(0.1, 0, 0, 0.208186, 0.01)
sim.animation()
