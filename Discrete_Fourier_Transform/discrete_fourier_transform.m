clc;clear all; close all; 
 
%Code by: circuitpotato
%Visit downtothecircuits.wordpress.com for more information
 
%Purpose: This code example shows the conversion of a time domain sampled 
%signal to frequency domain using Discrete Fourier Transform
 
%Input Specifications 
N = 1000;   % samples
Fs = 40e3;  % Nyquist Frequency / Sampling Frequency
f1 = 13e3;  % signal frequency 1
f2 = 10e3;  % signal Frequency 2
amp_1 = 3;  % signal amplitude 1
amp_2 = 1;  % signal amplitude 2
 
%White noise specifications
mu = 0;     % mean
std = 1;    % standard deviation
white_noise = std*randn(1,N)+mu;
 
%x-axis Specifications (Best not to change)
Ts = 1/Fs;  % Sampling Period 
dt = 0:Ts:(N-1)*Ts; % start:step:stop
 
x = amp_1*sin(2*pi*f1*dt)+amp_2*sin(2*pi*f2*dt)+white_noise;  % required signal + white noise
 
ReX = zeros(N/2,1);
ImX = zeros(N/2,1);
for k = 0:(N-1)/2
  for n = 0:N-1
    ReX(k+1) = ReX(k+1) + x(n+1)*cos((2*pi*k*n)/N); % real part
    ImX(k+1) = ImX(k+1) + x(n+1)*sin((2*pi*k*n)/N); % imaginary part 
  end
end
 
magnitude=zeros(N/2,1);
for q=1:N/2
  magnitude(q) = sqrt(ReX(q)^2+ImX(q)^2);
end
 
y_axis = magnitude./(N/2);   % peak amplitude values
x_axis = 0:Fs/N:((N/2)-1)*(Fs/N);   % frequency scale 
 
figure(1);
plot(x);
title('time domain sampled signal');
xlabel('Samples');
ylabel('Amplitude');
 
figure(2);
plot(x_axis,y_axis)
xlabel('Frequency');
ylabel('Amplitude');
title('Frequency Spectrum');
