#!/bin/bash
# Update Agent for PepsiPi!

echo "Updater has started"
git fetch
git reset --hard HEAD
git merge origin/main
python main.py
