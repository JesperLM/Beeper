from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np

class  FFTWidget(pg.GraphicsWindow):
    pg.setConfigOption('background', '#F0F0F0')
    pg.setConfigOption('foreground', 'k')
    def __init__(self, parent=None, **kargs):
        pg.GraphicsWindow.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle('FFT Plot')
        p1 = self.addPlot(title='FFT Plot', labels =  {'left':'Magnutude [W/m^2]', 'bottom':'Frequenzy [Hz]'})
        p1.setMenuEnabled(False)

        fillBrush = QtGui.QBrush(pg.mkColor(200, 0 , 0))

        curvePen1 = pg.mkPen(color=(200, 0 , 0), width=2)

        self.freqMag = np.zeros(569)
        self.freqs = np.linspace(100,10000,num=569)

        self.curve1 = p1.plot(self.freqs, self.freqMag, pen=curvePen1, brush=fillBrush, fillLevel=0)

        p1.setXRange(100, 1500, padding=0)
        p1.setYRange(0, 100, padding=0)
        
    def update(self, freqs, freqMag):
        self.xdata = freqs
        self.ydata = freqMag 
        self.curve1.setData(self.xdata, self.ydata)

class  dBWidget(pg.GraphicsWindow):
    pg.setConfigOption('background', '#F0F0F0')
    pg.setConfigOption('foreground', 'k')
    def __init__(self, parent=None, **kargs):
        pg.GraphicsWindow.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle('dB Plot')
        p1 = self.addPlot(title='Decibel over time', labels =  {'left':'Noice [dB]', 'bottom':'Time [s]'})  
        p1.setMenuEnabled(False)

        curvePen1 = pg.mkPen(color=(200, 0 , 0), width=2)
        curvePen2 = pg.mkPen(color=(0, 0 , 200), width=1, style=QtCore.Qt.DashLine)

        self.dBHistory = np.zeros(360001)
        self.time = np.linspace(0, 36000, num=360001)

        self.curve1 = p1.plot(self.time, self.dBHistory, pen=curvePen1)
        self.curve2 = p1.plot([0, 36000], [55, 55], pen=curvePen2)

        p1.setXRange(0, 10, padding=0)
        p1.setYRange(0, 100, padding=0)
        
    def update(self, timeHist, dBHist, dBBeep):
        self.xdata = timeHist
        self.ydata = dBHist 
        if (len(self.xdata)!=len(self.ydata)):
            self.ydata = np.append(self.ydata, [0])
        self.curve1.setData(self.xdata, self.ydata)
        self.curve2.setData([0, 36000], [dBBeep, dBBeep])


if __name__ == '__main__':
    w1 = FFTWidget()
    w1.show()
    w2 = dBWidget()
    w2.show()
    QtGui.QApplication.instance().exec_()