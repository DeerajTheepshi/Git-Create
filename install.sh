#!/bin/bash

BASE_DIR=`pwd`
echo "BASE_DIR = " "'"$BASE_DIR"'" >> info.py
read -p "Your GitHub User ID: " user_id
read -p "Your Github password: " user_pass
echo "USER_PASS = " "'"$user_pass"'">>info.py
echo "USER_ID = " "'"$user_id"'" >> info.py

echo '#!/bin/bash'>>gitc.sh
CMD="$(echo $BASE_DIR'/script.py'|sed 's/\ /\\ /g')"
echo $CMD
echo 'python '$CMD >>gitc.sh

txt='export PATH=$PATH:'
BASE_PATH="$(echo $BASE_DIR|sed 's/\ /\\ /g')"
echo $txt$BASE_PATH >> ~/.bashrc

chmod 777 gitc.sh
