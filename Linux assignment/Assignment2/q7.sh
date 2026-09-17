#!/bin/bash

echo "Name of the students who scored 80 or above 80: " 

while IFS=',' read -r name marks
do
if [ "$marks" -ge 80 ]
then
echo "Name = $name
Marks = $marks"
fi
done < students.csv
