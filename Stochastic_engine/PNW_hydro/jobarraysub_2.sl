#!/bin/bash

#SBATCH -p general
#SBATCH -N 1
#SBATCH --mem-per-cpu=4000
#SBATCH -n 6
#SBATCH -t 1-23:00:00



python simulation.py
