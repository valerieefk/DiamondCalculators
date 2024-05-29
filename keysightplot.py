import h5py 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import HDFStore
import tables as tables 

# Define your file. 
filename = r"C:\Users\valerief\Documents\GitHub\Scratch\sourceData\algan_1_vb8V_neg.h5"

# # Open the file.
df = h5py.File(filename)

# # What are the names of the data columns? 
print(df.keys())

h5_back = h5py.File(df, 'r')
h5_back['/Waveforms']


# # Import the file Method 2 
# f = h5py.File(filename, "r")

# # What HDF5 groups exist?  
# for key in f.keys():
#     print(key) #Names of the root level object names in HDF5 file - can be groups or datasets.
#     print(type(f[key])) # get the object type: usually group or dataset

# #Get the HDF5 group; key needs to be a group name from above
# group = f[key]

# #Checkout what keys are inside that group.
# for key in group.keys():
#     print(key)

# # This assumes group[some_key_inside_the_group] is a dataset, 
# # and returns a np.array:
# data = group[Waveforms][()]
# #Do whatever you want with data

# #After you are done
# f.close()

# # Import the file Method 1
# with h5py.File(filename, "r") as f:
#     # Print all root level object names (aka keys) 
#     # these can be group or dataset names 
#     print("Keys: %s" % f.keys())
#     # get first object name/key; may or may NOT be a group
#     a_group_key = list(f.keys())[0]

#     # get the object type for a_group_key: usually group or dataset
#     print(type(f[a_group_key])) 

#     # If a_group_key is a group name, 
#     # this gets the object names in the group and returns as a list
#     data = list(f[a_group_key])

#     # If a_group_key is a dataset name, 
#     # this gets the dataset values and returns as a list
#     data = list(f[a_group_key])
#     # preferred methods to get dataset values:
#     ds_obj = f[a_group_key]      # returns as a h5py dataset object
#     # ds_arr = f[a_group_key][()]  # returns as a numpy array



print("I did it.")
