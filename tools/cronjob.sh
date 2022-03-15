#!/bin/bash

echo "$(date)" 

source /home/ec2-user/miniconda3/bin/activate
conda activate cryptoenv

cd /home/ec2-user/surfingcrypto
echo "### PYTHON MAIN"
python main.py

conda deactivate
