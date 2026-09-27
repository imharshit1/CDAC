read -p"Enter the name of the directory: " dname
read -p"Enter the file extension: " fexe
cd "$dname"
files=$(ls *"$fexe")
count=$(echo "$files" | wc -l)

echo "All the files have $fexe extension: $files"
echo "Total number of files with $fexe extension : $count"
