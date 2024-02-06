import numpy as np
import matplotlib.pyplot as plt
 
#Code by: circuitpotato
#Visit downtothecircuits.com for more information
 
#Purpose: This code example shows us how a moving average filter works
#It is advisable to play with the different specifications to get a feel of
#how sampling works.
 
#Input Specifications
samples = 1000;  # No. of samples/points shown on graph
Fs = 20e3; # Nyquist Frequency / Sampling Frequency
f_signal = 100;  # signal frequency
amp_signal = 1; # signal amplitude
 
#White Noise Specification
mu = 0  # mean
std = 1 # standard deviation
white_noise = np.random.normal(mu, std, size=samples)
 
#x-axis Specifications (Best not to change)
p_nyquist=1/Fs   # Sampling period
dt=np.arange(0,(samples)*p_nyquist,p_nyquist)
 
#signal specifications
signal_clean=amp_signal*np.sin(2*np.pi*f_signal*dt)
signal_noisy=amp_signal*np.sin(2*np.pi*f_signal*dt)+white_noise
 
#Moving Average Specifications
averaged_points=32
leftover_samples=samples-averaged_points + 1    # Best not to change
 
#Nested for loop
move_ave=[]
for p in range(0,leftover_samples):
    total=0 # ensure "total" is empty first
    for q in range(0,averaged_points-1):
        total=signal_noisy[p+q]+total   # sum of all samples (accumulator)
    move_ave.append(total/averaged_points)  # Desired Moving Average
 
#plot your life away
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
 
plt.figure(3)
plt.plot(move_ave)  # Output of Noisy Signal through Moving Average Filter
plt.title('Filtered (Moving Average) Signal')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
 
plt.show()
