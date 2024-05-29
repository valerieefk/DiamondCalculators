#DiamondCalc.py created 2/27/2023 by BWM and EGM
#program to calculate heat load and current in diamond devices

import numpy as np
import os
import matplotlib.pyplot as plt
import math
cwd = os.getcwd()

##############################################
#Get elemental data in and properly formed
##############################################
# Just use these 
carbon = np.loadtxt((cwd + "/sourceData/carbon.txt"), dtype = float,comments ="#",)
pt = np.loadtxt((cwd + "/sourceData/pt.txt"), dtype = float,comments ="#",)
al = np.loadtxt((cwd + "/sourceData/al.txt"), dtype = float,comments ="#",)
# Diamond and metal thickness baked in 
carbonT = np.loadtxt((cwd + "/sourceData/carbonTrans.txt"), dtype = float,comments ="#",)
ptT = np.loadtxt((cwd + "/sourceData/PtTrans.txt"), dtype = float,comments ="#",)
alT = np.loadtxt((cwd + "/sourceData/alTrans.txt"), dtype = float,comments ="#",)
###############################################
# Constants
###############################################
densC = 3.15 #g/cm^3
densPt = 21.4 #g/cm^3
densAl = 2.7 #g/cm^3
enConv = 1.60218e-19 #eV per Joule
coulPerElec =  6.28e18  #elec per s for amp
micro_cm = 1e-4 # microns to cm conversion
nano_cm = 1e-7 # nm to cm conversion
ToMev= 1e-6
freeCarrier = 13.2 #energy to make electorn whole pairs in diamond
################################################

# Use these 
def MAdevice_perf_al (diamon_thick, metal_thick,energy, flux):
    bias = 10 # bias on dimaond
    coefAl = np.interp((energy*ToMev), al[:,0], al[:,2]) # interpolates the data from NIST 
    coefC = np.interp((energy*ToMev), carbon[:,0], carbon[:,2])
    transAl = (math.exp(-coefAl*metal_thick*nano_cm*densAl))   # Calculates transmission
    # Does subtractions of flux through layers 
    ptLayerAbs = (flux * (1-transAl))
    flux_to_diamond =flux-ptLayerAbs
    transC = (math.exp(-coefC*diamon_thick*micro_cm*densC))
    cLayerAbs = flux_to_diamond * (1-transC) # Assumes this is what diamond layer absorbs 
    current = (cLayerAbs * energy * enConv/ (freeCarrier)) # Turn in to current. 1 s integ.
    absHeat = (ptLayerAbs * 2 + cLayerAbs) * energy * enConv # in Joules, absorbed heat 
    jouleHeat = current * bias # IV = joule heating 
    heatLoad = absHeat + jouleHeat 
    absAlall = (1-transAl) * 2
    absC = 1-transC
    return current , heatLoad, absAlall, absC  

def MAdevice_perf_pt (diamon_thick, metal_thick,energy, flux):
    bias = 10 # bias on dimaond
    coefC = np.interp((energy*ToMev), carbon[:,0], carbon[:,2])
    coefPt = np.interp((energy*ToMev), pt[:,0], pt[:,2])
    transPt = (math.exp(-coefPt*metal_thick*nano_cm*densPt))
    ptLayerAbs = (flux * (1-transPt))
    flux_to_diamond =flux-ptLayerAbs
    transC = (math.exp(-coefC*diamon_thick*micro_cm*densC))
    cLayerAbs = flux_to_diamond * (1-transC)
    current = (cLayerAbs * energy * enConv/ (freeCarrier))
    absHeat = (ptLayerAbs * 2 + cLayerAbs) * energy * enConv
    jouleHeat = current * bias
    heatLoad = absHeat + jouleHeat 
    absPtall = (1-transPt) * 2
    absC = 1-transC
    return current , heatLoad, absPtall, absC

def Tran_device_perf_pt (energy, flux):
    bias = 10 #bias on dimaond
    coefC = np.interp((energy), carbonT[:,0], carbonT[:,1])
    coefPt = np.interp((energy), ptT[:,0], ptT[:,1])
    ptLayerAbs = (flux * (1-coefPt))
    flux_to_diamond =flux-ptLayerAbs
    cLayerAbs = flux_to_diamond * (1-coefC)
    current = (cLayerAbs * energy * enConv) /(freeCarrier)
    absHeat = (ptLayerAbs * 2 + cLayerAbs) * energy * enConv
    jouleHeat = current * bias
    heatLoad = absHeat + jouleHeat 
    absPtall = (1-coefPt)*2
    absC = 1-coefC
    return current , heatLoad, absPtall, absC

def Tran_device_perf_al (energy, flux):
    bias = 10 #bias on dimaond
    coefC = np.interp((energy), carbonT[:,0], carbonT[:,1])
    coefAl = np.interp((energy), alT[:,0], alT[:,1])
    alLayerAbs = (flux * (1-coefAl))
    flux_to_diamond =flux-alLayerAbs
    cLayerAbs = flux_to_diamond * (1-coefC)
    current = (cLayerAbs * energy * enConv)/(freeCarrier)
    absHeat = (alLayerAbs * 2 + cLayerAbs) * energy * enConv
    jouleHeat = current * bias
    heatLoad = absHeat + jouleHeat 
    absAlall = (1-coefAl)*2
    absC = 1-coefC
    return current , heatLoad, absAlall, absC

def main():
    # (diamond in um, metal in nm, E in eV, flux in photons/s)
    MAnumHigh = MAdevice_perf_pt(40,30,10000,1e15)
    # MAnumlow = MAdevice_perf_al(40,100,8000,1e15)
    # MAdevice_perf_al (diamon_thick, metal_thick,energy, flux)
    
    # At that energy in eV and a flux of whatever, it returns the same 4 things. Results the same as above but for the other dataset.) 
    tranHigh = Tran_device_perf_pt (5000,1e16)
    # tranLow = Tran_device_perf_al (8000,1e15)
    # Tran_device_perf_al (energy, flux) 
    # print ("\nMass atenuation method high energy current is {:e} A, heat {:e} W.\n low energy current {:e} A, heat {:e} W\n".format(MAnumHigh[0],MAnumHigh[1],MAnumlow[0],MAnumlow[1]))
    # print ("Transmission method high energy current is {:e} A, heat {:e} W.\n low energy current {:e} A, heat {:e} W\n".format(tranHigh[0], tranHigh[1], tranLow[0], tranLow[1])) 
    print(MAnumHigh)
    print(tranHigh[1])
   

#
#
#
if __name__ == "__main__":


   main()
   

