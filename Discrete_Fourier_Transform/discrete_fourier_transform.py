import numpy as np
import matplotlib.pyplot as plt
 
#Code by: circuitpotato
#Visit downtothecircuits.com for more information
 
#Purpose: This code example shows the conversion of a time domain sampled
#signal to frequency domain using Discrete Fourier Transform
 
#Input Specifications
N = 1000;   # samples
Fs = 40e3;  # Nyquist Frequency / Sampling Frequency
f1 = 13e3;  # signal frequency 1
f2 = 10e3   # signal frequency 2
amp_1 = 3;  # signal amplitude 1
amp_2 = 1   # signal amplitude 2
 
#White Noise Specification
mu = 0  # mean
std = 1 # standard deviation
white_noise = np.random.normal(mu, std, size=N)
 
#x-axis Specifications (Best not to change)
Ts=1/Fs   # Sampling period
dt=np.arange(0,(N)*Ts,Ts)   # np.arange(start,stop,step)
 
x=amp_1*np.sin(2*np.pi*f1*dt)+amp_2*np.sin(2*np.pi*f2*dt)+white_noise   # required signal + white noise
 
ReX = np.zeros((int(N/2),1))
ImX = np.zeros((int(N/2),1))
for k in range(0,int(N/2)):
    for n in range(0,N):
        ReX[k] = ReX[k] + x[n]*np.cos((2*np.pi*k*n)/N)  # real part
        ImX[k] = ImX[k] + x[n]*np.sin((2*np.pi*k*n)/N)  # imaginary part
 
magnitude=np.zeros((int(N/2),1))
for q in range(0,int(N/2)):
    magnitude[q]=np.sqrt((ReX[q]**2)+(ImX[q]**2))
 
y_axis=magnitude/(N/2)   # peak amplitude values
x_axis=np.arange(0,(N/2)*(Fs/N),(Fs/N)) # frequency values
 
plt.figure(1)
plt.plot(x)
plt.title('time domain sampled signal')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
 
plt.figure(2)
plt.plot(x_axis,y_axis)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')
 
plt.show()
