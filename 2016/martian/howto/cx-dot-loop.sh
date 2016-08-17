#!/bin/bash

filename="json-gv/*.json"

for file in $filename
do
 java -jar collatex-tools-1.7.1.jar --algorithm dekker --format dot --output $file.gv $file
done
