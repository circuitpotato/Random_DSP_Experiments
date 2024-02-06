clc; clear all; close all; 
%Code by: circuitpotato
%Visit downtothecircuits.com for more information 
 
%Purpose: This code example shows us how a moving average filter works
%It is advisable to play with the different specifications to get a feel of
%how sampling works. 
 
%Input Specifications
samples = 1000;  % No. of samples/points shown on graph 
Fs = 20e3; % Nyquist Frequency / Sampling Frequency
f_signal = 100; % signal frequency
amp_signal = 1; % signal amplitude
 
%White noise specifications
mu=0;
std = 1;
white_noise = std*randn(1,samples)+mu;
 
%x-axis Specifications (Best not to change)
p_nyquist = 1/Fs;  % Sampling Period 
dt = 0:p_nyquist:(samples-1)*p_nyquist; 
 
%signal specifications
signal_clean = amp_signal*sin(2*pi*f_signal*dt);   
signal_noisy = amp_signal*sin(2*pi*f_signal*dt)+white_noise;
 
%Moving Average Specifications
averaged_points=32;
leftover_samples=samples-averaged_points + 1;   % Best not to change
 
%Nested for loop
for p = 1:leftover_samples
    total(p) = 0; % ensure "total" is empty first 
    for q = 0:(averaged_points-1)  
        total(p) = signal_noisy(p+q) + total(p);  % sum of all samples (accumulator)
    end
    move_ave(p) = (total(p))/averaged_points; % Desired Moving Average
end
 
%plot your life away
figure(1);
plot(signal_clean); % Clean Signal
title('Clean Sampled Signal');
xlabel('Samples');
ylabel('Amplitude');
 
figure(2);
plot(signal_noisy); % Noisy Signal
title('Noisy Sampled Signal');
xlabel('Samples');
ylabel('Amplitude');
 
figure(3);
plot(move_ave); % Output of Noisy Signal through Moving Average Filter
title('Filtered (Moving Average) Signal');
xlabel('Samples');
ylabel('Amplitude');
