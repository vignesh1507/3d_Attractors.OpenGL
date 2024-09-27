import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
import pyqtgraph.opengl as gl
import sys


class Simulation():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = gl.GLViewWidget()     
        self.window.setGeometry(100, 100, 800, 600) 
        self.window.setWindowTitle("I am going to draw a line") 
        self.window.show()

        self.points_list = []  # Use an instance variable instead of global
        self.draw()

    def draw(self):
        point1 = (0, 0, 0)  
        point2 = (5, 6, 8)  

        self.points_list.append(point1)
        self.points_list.append(point2)
        print(self.points_list)
        points_array = np.array(self.points_list) 
        drawing_variable = gl.GLLinePlotItem(pos=points_array, width=1, antialias=True)
        self.window.addItem(drawing_variable)

    def start(self):
        QtWidgets.QApplication.instance().exec_()  # Run the window properly

Simulation().start()
