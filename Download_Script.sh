#!/bin/sh
#SBATCH --job-name=tensorflow
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=16:00:00

cd data
wget data.csail.mit.edu/places/places365/train_256_places365standard.tar
cd ..
conda install -c anaconda tensorflow-gpu
