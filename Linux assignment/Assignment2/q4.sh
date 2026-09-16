read -p"Enter the name of directory: " dname

if [ -d "$dname" ]
then
cd "$dname"
else
mkdir "$dname"
cd "$dname"
fi

read -p"Enter the name of the five files: " f1name f2name f3name f4name f5name
touch "$f1name" "$f2name" "$f3name" "$f4name" "$f5name"
ls

count=$(find . -type f | wc -l)
echo "Number of files: $count" 
