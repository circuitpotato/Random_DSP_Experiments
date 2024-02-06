clc; clear all; close all; 
%Code by: circuitpotato
%Visit downtothecircuits.wordpress.com for more information 
 
%Purpose: This code example shows us how to sample a sine wave signal.
%It is advisable to play with the different specifications to get a feel of
%how sampling works. 
 
%Input Specifications
samples = 100;  % No. of samples/points shown on graph 
Fs = 20e3; % Nyquist Frequency / Sampling Frequency
f_signal = 1e3; % signal frequency
amp_signal = 1; % signal amplitude
 
%White noise specifications
mu=0;   % mean
std = 1;    % standard deviation
white_noise = std*randn(1,samples)+mu;
 
%x-axis Specifications (Best not to change)
p_nyquist = 1/Fs;  % Sampling Period 
dt = 0:p_nyquist:(samples-1)*p_nyquist; 
 
signal_clean = amp_signal*sin(2*pi*f_signal*dt);    % clean sine wave
signal_noisy = amp_signal*sin(2*pi*f_signal*dt)+white_noise;    %sine wave affected by white noise
 
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
