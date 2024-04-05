import soundfile as sf
from scipy import signal, fft
import numpy as np
from numpy.polynomial import Polynomial as P
from matplotlib import pyplot as plt

def myfiltfilt(b, a, input_signal):
    # Forward filter
    filtered_signal = signal.lfilter(b, a, input_signal)
    
    # Reverse filter the forward filtered signal
    reverse_filtered_signal = signal.lfilter(b, a, filtered_signal[::-1])[::-1]
    
    return reverse_filtered_signal

# Read .wav file 
input_signal, fs = sf.read('saipoorna.wav') 

# Sampling frequency of Input signal
sampl_freq = fs

# Order of the filter
order = 4   

# Cutoff frequency 5kHz
cutoff_freq = 5000.0  

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

# Filter the input signal with butterworth filter using built-in function
output_signal = signal.filtfilt(b, a, input_signal, padlen=1)

# Filter the input signal with your custom filter function
op1 = myfiltfilt(b, a, input_signal)

# Plotting
x_plt = np.arange(len(input_signal))
plt.plot(x_plt[1000:10000], output_signal[1000:10000], 'blue', label='Output by built-in function')
plt.plot(x_plt[1000:10000], op1[1000:10000], 'red',label='Output by custom function')
plt.title("Verification of outputs of Audio Filter")
plt.grid()
plt.legend()
plt.savefig("Audio_Filter_verification.png")

