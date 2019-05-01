"""
Module to calculate dB vs time and FFT of sound recorded from the microphone.

This module also plays a sound if the audiolevel is above a given threshold value.

API overview:
    listenAudio
    stopAudio
    audioCallback
    playBeep
"""
import numpy as np
import sounddevice as sd
import time
from playsound import playsound
from threading import Thread

class AudioLevel:
    """
    Module to calculate dB vs time and FFT of sound recorded from the microphone.
    This module also plays a sound if the audiolevel is above a given threshold value.
    """
    def __init__(self, dBBeep=20, dBCalibrate=-38):
        """
        Initializes the AudioLevel class.

        the class takes two optional inputs. These inputs are dBBeep which sets the 
        decible threshold level for the beep function and a input for dBCalibrate which 
        is the calibration level for the microphone.
        """
        self.dBBeep = dBBeep
        self.dBCalibrate = dBCalibrate
        self.playing = 0
        self.listening = False
        self.dBLevel = 0
        self.freqMag = np.zeros(569)
        self.freqs = np.linspace(100,10000,num=569)
        self.timeHistory = np.linspace(0, 36000, num=360001)
        self.dbHistory = np.zeros(360001)

    def playBeep(self):
        """
        This function plays a Beep when called.
        """
        self.playing = 1       # Set to 1 when sound is playing
        playsound('quieter.wav')
        self.playing = 0       # Set to 0 when sound is finished

    def audioCallback(self, indata, frames, time, status):
        """Function to listen for sound volume and play sound if sound is to high."""
        freqFFT = np.fft.rfft(indata[:,1])  # Extract positive frequencies of sound
        self.freqMag = np.abs(freqFFT) * 2       # Multiply with 2 since half of the frequency band has been removed
        power = np.trapz(self.freqMag, x=self.freqs)  # Integrate frequency respone to get power level to calulate dB
        self.dBLevel = 20 * np.log10(power) + self.dBCalibrate # Calculate the decible level for the sound, microphone calibrated at -38dB
        self.dbHistory = np.delete(self.dbHistory,-1)
        self.dbHistory = np.insert(self.dbHistory,0,self.dBLevel)

        if ( self.dBLevel > self.dBBeep and self.playing == 0):
            t = Thread(target=self.playBeep)       # Play sound in parallel thread
            t.start()
    
    def listenAudio(self):
        """Starts to listens for audio level every 0.25 second."""
        self.listening = True
        stream = sd.InputStream(callback=self.audioCallback)  # listen to microphone and call audio_callback
        with stream:
            while self.listening:
                time.sleep(0.25)
            return
            
    def stopAudio(self):
        """Stops to listens for audio level."""
        self.listening = False