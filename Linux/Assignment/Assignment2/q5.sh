read -p"Enter the name of the directory: " dname
read -p"Enter the file extension: " fex

cd "$dname"
ls "*$fex"
