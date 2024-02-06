import numpy as np
import matplotlib.pyplot as plt
 
#Code by: circuitpotato
#Visit downtothecircuits.wordpress.com for more information
 
#Purpose: This code example shows us how to sample a sine wave signal.
#It is advisable to play with the different specifications to get a feel of
#how sampling works.
 
#Input Specifications
samples = 100;  # No. of samples/points shown on graph
Fs = 20e3; # Nyquist Frequency / Sampling Frequency
f_signal = 1e3;  # signal frequency
amp_signal = 1; # signal amplitude
 
#White Noise Specification
mu = 0  # mean
std = 1 # standard deviation
white_noise = np.random.normal(mu, std, size=samples)
 
#x-axis Specifications (Best not to change)
p_nyquist=1/Fs   # Sampling period
dt=np.arange(0,(samples)*p_nyquist,p_nyquist)
 
signal_clean=amp_signal*np.sin(2*np.pi*f_signal*dt) # clean sine wave
signal_noisy=amp_signal*np.sin(2*np.pi*f_signal*dt)+white_noise # sine wave affected by white noise
 
plt.figure(1)
plt.plot(signal_clean)  # Clean Signal
plt.title('Clean Sampled Signal')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
 
plt.figure(2)
plt.plot(signal_noisy)  # Noisy signal
plt.title('Noisy Sampled Signal')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
 
plt.show()
