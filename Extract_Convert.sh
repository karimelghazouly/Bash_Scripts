#!/bin/sh
#SBATCH --job-name=tensorflow
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=16:00:00

python3 Convert.py
