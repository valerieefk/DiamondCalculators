#DiamondCalc.py created 2/27/2023 by BWM and EGM
#program to calculate heat load and current in diamond devices

import numpy as np
import os
import matplotlib.pyplot as plt
import sys
import pandas as pd
import math
cwd = os.getcwd()

##############################################
#Get elemental data in and properly formed
##############################################
carbon = np.loadtxt((cwd + "/scratch/sourceData/carbonTrans.txt"), dtype = float,comments ="#",)
pt = np.loadtxt((cwd + "/scratch/sourceData/PtTrans.txt"), dtype = float,comments ="#",)
# al = np.loadtxt((cwd + "/scratch/al.txt"), dtype = float,comments ="#",)
spectrum = np.loadtxt((cwd +"/scratch/sourceData/CLS_WB_Spec_With_Filter.txt"), dtype = float, skiprows = 5,)
#spectrum2 = np.loadtxt((cwd +"/scratch/sourceData/CLS_WB_Spec_WO_Filter.txt"), dtype = float, skiprows = 100,)
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
kToMev= 1e-3
freeCarrier = 13.2 #energy to make electorn whole pairs in diamond
################################################

diamondThick = 40 * micro_cm
dimaondEn = 4
diamondFlux = 1e13
ptThick = 30 * nano_cm
def ftoCurrentC (thick,energy,flux): #thickness in cm
    coef = np.interp(energy, carbon[:,0], carbon[:,2])
    current = (flux * (math.exp(-coef*thick*densC)))
    return current

# def device_perf_al (diamon_thick, metal_thick,energy, flux):
#     bias = 10 #bias on dimaond
#     coefC = np.interp((energy*kToMev), carbon[:,0], carbon[:,2])
#     coefal = np.interp((energy*kToMev), al[:,0], al[:,2])
#     alLayerAbs = (flux * (1-(math.exp(-coefal*metal_thick*densAl))))
#     flux_to_diamond =flux-alLayerAbs
#     cLayerAbs = flux_to_diamond * (1-(math.exp(-coefC*diamon_thick*densC)))
#     current = (cLayerAbs * energy*1000/ (freeCarrier))*coulPerElec
#     absHeat = (alLayerAbs * 2 + cLayerAbs)*enConv
#     jouleHeat = current * bias
#     heatLoad = absHeat + jouleHeat 

#     return current , heatLoad

def device_perf_pt (energy, flux):
    bias = 10 #bias on dimaond
    coefC = np.interp((energy), carbon[:,0], carbon[:,1])
    coefPt = np.interp((energy), pt[:,0], pt[:,1])
    ptLayerAbs = (flux * (1-coefPt))
    flux_to_diamond =flux-ptLayerAbs
    cLayerAbs = flux_to_diamond * (1-coefC)
    current = (cLayerAbs *1000  /(freeCarrier*coulPerElec))
    absHeat = (ptLayerAbs * 2 + cLayerAbs)*1000*enConv
    jouleHeat = current * bias
    heatLoad = absHeat + jouleHeat 
   # heatLoad = absHeat
    return current , heatLoad


# current = ftoCurrentC(diamondThick,dimaondEn,diamondFlux)
# currentDev = device_perf_pt(diamondThick,ptThick,20,diamondFlux)
# print ("{:e}".format(current))
# exp = math.exp(-2.238E-01*densC*diamondThick)
# print(1-exp)
# print ("{:e},{:e}".format(currentDev[0],currentDev[1]))
# currentDev4 = device_perf(diamondThick,ptThick,4,diamondFlux)

# print ("{:e}".format(currentDev4))
# energy = dimaondEn
# coef = np.interp(energy, carbon[0,:], carbon[2,:])
# print(coef)

# x= spectrum[:,0]
# y= spectrum[:,1]
# x1= spectrum2[:,0]
# y1= spectrum2[:,1]
# plt.plot(x,y)
# plt.plot(x1,y1)
# plt.show()
totalHeat = np.zeros((len(spectrum),1), dtype=float)
totalCurrent = np.zeros((len(spectrum),1), dtype=float)
# spectrum[:,0] = spectrum[:,0]/1000
for index in range(len(spectrum)):
    singePoint = device_perf_pt((spectrum[index,0]),spectrum[index,1])
    totalHeat[index,0] = singePoint[1]
    totalCurrent[index,0] = singePoint[0]

print("beam power is {}".format(np.sum(spectrum[:,1])*1000*enConv))
print ("Total Current is {:e}.\n Total Heat is {:e}".format(np.sum(totalCurrent),np.sum(totalHeat)))
   

   
#
#
#
# if __name__ == "__main__":


#    main(sys.argv[1:])
   

