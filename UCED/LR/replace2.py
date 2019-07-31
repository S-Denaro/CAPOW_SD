
"""
Created on Tue Dec  4 14:20:33 2018

@author: sdenaro
"""

import os
from shutil import copy

for run in range(0,1200):

    #these lines create the directory in case it didn't exist
    path=os.getcwd()+'\\PNW' + str(run)
    os.makedirs(path,exist_ok=True)

    #these lines copy the update files into the given path
    path=os.getcwd()+'\\PNW' + str(run)+'\\'+'UCED'
    #modify and add the path if needed
    update='PNW_wrapper.py'
    update_2='CA_wrapper.py'
    copy(update,path)
    copy(update_2,path)
