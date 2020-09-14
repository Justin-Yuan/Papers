#!/bin/bash

# hack to make conda works in bash script 
# https://github.com/conda/conda/issues/7980
source ~/anaconda3/etc/profile.d/conda.sh

# download notion data zip file, check ~/.notion_config for token_v2 
echo "downloading notion backup..."
conda activate misc 
# simulate "Enter" keypress for 1st workspace to backup
# https://stackoverflow.com/questions/6264596/simulating-enter-keypress-in-bash-script
# echo -ne '\n' | <yourfinecommandhere>
# echo | <yourfinecommandhere>
yes "" | backup_notion --output-dir='.'
export_file=$(ls | grep export)

# risky step...
echo "updating notion data..."
rm -rf notion_data/*
unzip $export_file -d notion_data

# clean up 
rm $export_file
conda deactivate  

# update git 
echo "updating git..."
git status .
git add notion_data/* 
backup_date=$(date)
git commit -m "notion backup $backup_date"
git push origin master 

echo "notion backup done..."

