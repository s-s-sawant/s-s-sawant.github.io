#!/bin/bash

read -p "Enter commit msg" cmt

cd
ssh-add think_pad
cd git/s-s-sawant.github.io

git add --all
git commit -m "$cmt" 
git push origin master
