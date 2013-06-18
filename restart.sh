#!/bin/bash
#cd ~/python/webpycms/
find . -type f -name "*.pyc" | xargs rm -rf
python app.py
