import matplotlib.pyplot as plt 
import numpy as np
import sys

Scur = 762   # susceptible
Rcur = 0     # people recovered
Icur = 1     # people infected

trans_const = 0.00218   # infectiousness of disease: r = kb/N
recov_rate = 0.5        # recovery rate: a = 1/(# days infected)
simlength = 15          # number of days in simulation

resultarray = np.zeros((simlength,3))   # 2D array of floats 
resultarray[0,:] = Scur, Rcur, Icur     # record initial values

for i in range(1, simlength):
    new_infected = trans_const * Scur * Icur   # = rSI
    new_recovered = recov_rate * Icur          # = aI

    Scur = Scur - new_infected
    Icur = Icur + new_infected - new_recovered
    Rcur = Rcur + new_recovered

    resultarray[i,:] = Scur, Rcur, Icur
    
model_plot_title = f"SIR Model with r: {str(trans_const)}, a: {str(recov_rate)}"
plt.plot(resultarray[:,0], "k-", label = "Susceptible")
plt.plot(resultarray[:,1], "g^", label = "Recovered")
plt.plot(resultarray[:,2], "rd", label = "Infected")

plt.title(model_plot_title)
plt.ylabel("# People")
plt.xlabel("# Days")
plt.legend()

print("Susceptible,\tRecovered,\tInfected") 
for i in range(simlength):
    susceptible = f"{resultarray[i,0]:.6f}"
    recovered = f"{resultarray[i,1]:.6f}"
    infected = f"{resultarray[i,2]:.6f}"
    print(f"{susceptible},\t{recovered},\t{infected}")

plt.savefig(f"SIR_Model_r_{trans_const}_a_{recov_rate}.jpg")
plt.show()
