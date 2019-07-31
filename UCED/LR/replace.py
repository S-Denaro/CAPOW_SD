# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:04:22 2019

@author: sdenaro
"""

from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


for i in range(0,200):
    file_path='LR/CA'+str(i)+'/CA_dispatchLP.py'
    pattern='from __future__ import division'
    subst='from __future__ import division'
    replace(file_path, pattern, subst)

for i in range(0,200):
    file_path='CA/PNW'+str(i)+'/CA_wrapper.py'
    pattern='CAISO_result = opt.solve(instance)'
    subst='CAISO_result = opt.solve(instance,tee=True,symbolic_solver_labels=True)'
    replace(file_path, pattern, subst)
