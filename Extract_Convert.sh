
#!/bin/sh
#SBATCH --job-name=tensorflow
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=16:00:00

mkdir test-grey
mkdir test-colored
tar -xvf train_256_places365standard.tar
python3 Convert.py
