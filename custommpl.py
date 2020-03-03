from PyQt5.uic import loadUiType

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


Ui_MainWindow, QMainWindow = loadUiType('matplotlibGUI.ui')

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.fig_dict = {}

        self.mplfigs.itemClicked.connect(self.change_figure)
    
    def change_figure(self, item):
        text = item.text()
        self.remove_plot()
        self.add_plot(self.fig_dict[text])

    def add_fig(self, name, fig):
        self.fig_dict[name] = fig
        self.mplfigs.addItem(name)


    def add_plot(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, self.mplwindow, coordinates = True)
        self.mplvl.addWidget(self.toolbar)

    def remove_plot(self):
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvl.removeWidget(self.toolbar)
        self.toolbar.close()

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    
    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111)
    ax1f1.plot(np.random.rand(5))

    fig2 = Figure()
    ax1f2 = fig2.add_subplot(121)
    ax1f2.plot(np.random.rand(5))
    ax2f2 = fig2.add_subplot(122)
    ax2f2.plot(np.random.rand(10))

    fig3 = Figure()
    ax1f3 = fig3.add_subplot(111)
    ax1f3.pcolormesh(np.random.rand(20,20))

    main = Main()
    main.add_plot(fig1)
    main.add_fig("Figure 1", fig1)
    main.add_fig("Two Plots", fig2)
    main.add_fig("Colormesh", fig3)
    main.show()
    sys.exit(app.exec_())