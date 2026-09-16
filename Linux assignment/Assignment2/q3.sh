read -p"Enter the name of the directory: " dname
if [ -d "$dname" ]
then
echo "Directory already exist"

else 
mkdir "$dname"
echo "$dname created"
fi

cd "$dname"
ls
