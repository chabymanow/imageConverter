#! /usr/bin/bash
echo "Setting up convert file to run"
file="convert.py"
chmod u+x $file
echo "Move file to /usr/local/bin"
cp $file /usr/local/bin