#!/bin/bash

echo "###############"
echo "$(date)" 

source /home/ec2-user/miniconda3/bin/activate
conda activate cryptoenv

pip install surfingcrypto -U --quiet
pip install TelegramBotNotifications -U --quiet

cd /home/ec2-user/surfingcrypto

python main.py

conda deactivate
