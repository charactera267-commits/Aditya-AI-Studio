#!/usr/bin/env bash

# 1. Zip file ko extract (unzip) karo using Python
python -m zipfile -e Aditya-AI-Studio.zip .

# 2. Extracted folder ke andar se files ko bahar nikalo
mv Aditya-AI-Studio/* .

# 3. Python tools install karo
pip install -r requirements.txt
