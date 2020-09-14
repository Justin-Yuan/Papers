#!/bin/bash

# download notion data zip file
act misc 
# check ~/.notion_config for token_v2 
backup_notion --output-dir='.'
export_file=$(ls | grep export)

# risky step...
rm -rf notion_data/*
unzip $export_file -d notion_data

# clean up 
rm $export_file
deact 

# update git 
git status .
git add notion_data/* 
backup_date=$(date)
git commit -m "notion backup $backup_date"
git push origin master 

echo "notion backup done..."