# Pulse Parameters
vmax = 5  # volts
fc = 5e9  # GHz
bw = 50  # percent
v0 = 0.00001  # Maximum voltage allowed at t = 0
ptype = "normal"

# Time vector
t = linspace(0, 5e-9, 2001);

# Compute sigma (control's pulse width)
sigma = 1/(2*pi*(fc*bw/100)/2.354820045030949);

# Compute mu (time offset)
# Note that this is only approximate for the Differentiated Pulse.
mu = sigma*sqrt(-2*log(v0/vmax));

if ptype == "normal"
    pulse = vmax*exp.(-(t - mu).^2/(2*sigma^2));
elseif ptype == "diff"
    pulse = -vmax/sigma*(t - mu).*exp.(0.5-(t - mu).^2/(2*sigma^2));
elseif ptype == "sinmod"
    pulse = vmax*exp.(-(t - mu).^2/(2*sigma^2)).*cos.(2*pi*fc*(t - mu));
else
    error("Unsupported pulse type")
end

using PyPlot
plot(t*1e9, pulse, linewidth=2.0)
xlabel("Time (ns)")
ylabel("Amplitude (Volts)")
grid(true)
