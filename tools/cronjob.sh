#!/bin/bash

echo "###############"
echo "$(date)" 

source /home/ec2-user/miniconda3/bin/activate
conda activate cryptoenv

pip install surfingcrypto --upgrade
pip install TelegramBotNotifications --upgrade

cd /home/ec2-user/surfingcrypto

python main.py

conda deactivate
