"""
A Program to listen for audio level and play sound if dB level is to high.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import qtmodern.styles
import qtmodern.windows
import sys
import os
import ctypes

from audiolevel import AudioLevel
import ui_design

cwd = os.getcwd()

class BeeperApp(QtWidgets.QMainWindow, ui_design.Ui_MainWindow):
    """This is the class that handels the Qt GUI and its interactions for the Beeper App."""
    def __init__(self, parent=None):
        """Imports QT GUI and adds interactions and icons."""
        super(BeeperApp, self).__init__(parent)
        self.setupUi(self)
        # Set BG color and icon for App
        self.setWindowIcon(QtGui.QIcon(os.path.join(cwd, 'Trumpet.svg')))
        self.setStyleSheet("background-color: #F9F9F9;")
        # Set images on buttons
        self.btnStart.setIcon(QtGui.QIcon(os.path.join(cwd, 'Play.svg')))
        self.btnStart.setIconSize(QtCore.QSize(35,35))
        self.btnStart.setText('')
        self.btnStop.setIcon(QtGui.QIcon(os.path.join(cwd, 'Stop.svg')))
        self.btnStop.setIconSize(QtCore.QSize(35,35))
        self.btnStop.setText('')
        # Connect buttons to functions
        self.btnStart.clicked.connect(self.start_run)
        self.btnStop.hide()
        self.btnStop.clicked.connect(self.stop_run)
        self.audioLevel = AudioLevel()
        self.tPlott = None

    def start_run(self):
        """
        Thhis method is coupled to the run button.

        This method calls the local library 'audiolevel' 
        and starts to update the graphs for the FFT and dB levels calcualted in 'audiolevel'.

        It also hides the run button and shows the stop button.
        """
        noice = self.entryNoice.text()
        try:
            inNumberint = float(noice)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'The input for decibel cut-off needs to a number!\nYou typed: ' + noice, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return
        self.btnStart.hide()
        self.btnStop.show()
        self.audioLevel.dBBeep = inNumberint
        t1 = Thread(name='Listen', target=self.audioLevel.listenAudio)       # Play sound in parallel thread
        t1.start()
        self.graph_update()
        
    def stop_run(self):
        """
        This method is coupled to the stop button.

        This method stops the local library 'audiolevel'.

        It also shows the run button and hides the stop button.
        """
        self.audioLevel.stopAudio()
        self.btnStop.hide()
        self.btnStart.show()

    def graph_update(self):
        """
        This method is used to update the graphs used to visualize 
        the FFT and dB levels calcualted in 'audiolevel'.
        """
        timerFFT = QtCore.QTimer(self)
        timerFFT.timeout.connect(lambda: self.graphFFT.update(self.audioLevel.freqs, self.audioLevel.freqMag))
        timerFFT.start(50) 
        timerdB = QtCore.QTimer(self)
        timerdB.timeout.connect(lambda: self.graphdB.update(self.audioLevel.timeHistory, self.audioLevel.dbHistory, self.audioLevel.dBBeep))
        timerdB.start(50)


def main():
    """Initializes the Qt GUI for the Beeper App."""
    myappid = u'JesperLM.Beeper.0.01' # My App ID
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    form = BeeperApp()

    #qtmodern.styles.dark(app)
    #mw = qtmodern.windows.ModernWindow(form)
    #mw.show()

    form.show()
    app.exec_()


if __name__ == '__main__':
    main()