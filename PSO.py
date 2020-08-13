#Particle Swarm Optimization Algorithm
# by
# João Pedro Elger &
# Karine Faggian Franciscon

import random
import math
import matplotlib.pyplot as plt

maxx = 5 # X bound
maxy = 5 # Y bound

s = 500 # Number of Particles
iterations = 1000 # Number of Iterations
  
minimaxi = 0 # Minima = 0 | Maxima = 1

# c1 & c2 Constants
c1 = 2
c2 = 2

# Inertia component and its decrement
w = 0.95
decrement = 3*w/iterations

# Components of each particle
pbest = []
pbestx = []
pbesty = []
gbest = 0
vx = []
vy = []
presentx = []
presenty = []

# List of best values found while running the code
bestz = []

# Function to Find the Maxima or Minima
def fitnessfunction(x, y):
    z = -20.0*math.exp(-0.2*math.sqrt(0.5*(x*x + y*y))) - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20 # Ackley's function
    return z

# Particles Initialization
for i in range(s):
    presentx.append(random.uniform(-1, 1)*maxx)
    presenty.append(random.uniform(-1, 1)*maxy)
    pbestx.append(presentx[i])
    pbesty.append(presenty[i])
    vx.append(1)
    vy.append(1)
      
counter = 0
if(minimaxi):
    while(counter < iterations):
        bestz.append(fitnessfunction(pbestx[gbest], pbesty[gbest]))
        w -= decrement
        for i in range(s):   

            # Velocities Update
            vx[i] = w*vx[i] + c1 * random.uniform(-1, 1) * (pbestx[i] - presentx[i]) + c2 * random.uniform(-1, 1) * (pbestx[gbest] - presentx[i])
            vy[i] = w*vy[i] + c1 * random.uniform(-1, 1) * (pbesty[i] - presenty[i]) + c2 * random.uniform(-1, 1) * (pbesty[gbest] - presenty[i])
            
            # Positions Update
            presentx[i] = math.fmod((presentx[i] + vx[i]), maxx)
            presenty[i] = math.fmod((presenty[i] + vy[i]), maxy)

            # Best Position of Each Particle Update
            if(fitnessfunction(presentx[i], presenty[i]) > fitnessfunction(pbestx[i], pbesty[i])):
                pbestx[i] = presentx[i]         
                pbesty[i] = presenty[i]         

            # Global Best Position Update
            if(fitnessfunction(presentx[i], presenty[i]) > fitnessfunction(pbestx[gbest], pbesty[gbest])):         
                gbest = i

        
        counter += 1

    print("Maxima found: " + str(fitnessfunction(pbestx[gbest], pbesty[gbest])))


elif(not minimaxi):
    while(counter < iterations):
        bestz.append(fitnessfunction(pbestx[gbest], pbesty[gbest]))
        w -= decrement
        for i in range(s):   

            # Velocities Update
            vx[i] = w*vx[i] + c1 * random.uniform(-1, 1) * (pbestx[i] - presentx[i]) + c2 * random.uniform(-1, 1) * (pbestx[gbest] - presentx[i])
            vy[i] = w*vy[i] + c1 * random.uniform(-1, 1) * (pbesty[i] - presenty[i]) + c2 * random.uniform(-1, 1) * (pbesty[gbest] - presenty[i])
            
            # Positions Update
            presentx[i] = math.fmod((presentx[i] + vx[i]), maxx)
            presenty[i] = math.fmod((presenty[i] + vy[i]), maxy)

            # Best Position of Each Particle Update
            if(fitnessfunction(presentx[i], presenty[i]) < fitnessfunction(pbestx[i], pbesty[i])):
                pbestx[i] = presentx[i]         
                pbesty[i] = presenty[i]         

            # Global Best Position Update
            if(fitnessfunction(presentx[i], presenty[i]) < fitnessfunction(pbestx[gbest], pbesty[gbest])):         
                gbest = i
             
        counter += 1

    print("Minima Found: " + str(fitnessfunction(pbestx[gbest], pbesty[gbest])))

# Where the particle found the minima or maxima in XY plane
print("X: " + str(pbestx[gbest]))
print("Y: " + str(pbesty[gbest]))

# Convergency Graph
plt.subplots()
plt.plot(bestz)
plt.xlabel('Iterations')
plt.ylabel('Global Value')
plt.title('Convergency Graph')
plt.grid()
plt.show()