#!/bin/bash

# Define a timestamp function
timestamp() {
  date +"%T" # current time
}

cd
ssh-add priv
cd my_git/webpage/s-s-sawant.github.io

git add --all
git commit -m "Updated: `date +'%Y-%m-%d %H:%M:%S'`" # Updated: 2019-08-28 10:22:06
git push origin master