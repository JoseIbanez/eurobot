#!/bin/bash

cd ~/Projects/eurobot


while true
do
   uv run test_05.py

   echo
   echo "An error ?"
   date
   echo "Waiting 30sec"
   sleep 30
done




