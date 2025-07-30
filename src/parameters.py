# Parameters of the simulation
# by Erwan Le Doeuff (weld)

timesteps = 1000 # number of timesteps
dt = 0.01

box_size = 10

T = 1.0 #310.15 # 37°C

N = 5 # number of beads
b = 1.0 # length of kuhn segments
chain_length = (N-1)*b


k = 1.0 # spring constant
zeta = 1.0 # one-bead friction coefficient


k_B = 1.0 # 1.38e-23
sigma = (2*k_B*T/(zeta*dt))**0.5 # fluctuation-dissipation
