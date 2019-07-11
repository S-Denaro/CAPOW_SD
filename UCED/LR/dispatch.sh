#!/bin/bash

#SBATCH -p general
#SBATCH -N 1
#SBATCH -t 07-00:00:00
#SBATCH --mem=16g
#SBATCH -n 8


python wrapper_1_5.py
