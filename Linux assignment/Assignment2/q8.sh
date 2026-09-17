read -p "Enter the name of the directory to copy: " dname
if [ -d "$dname" ]
then
backup="backup_$(date +%Y%m%d_%H%M%S)"
mkdir "$backup"
cp "$dname"/*.txt "$backup"
echo "Copied Successfully"

else
echo "Directory not found"

fi
