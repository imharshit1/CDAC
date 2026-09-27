read -p"Enter the directory name: " dname
mkdir $dname

read -p"Enter the name of the first file: " f1name
read -p"Enter the name of the second file: " f2name
read -p"Enter the name of the third file: " f3name

cd $dname
touch $f1name
touch $f2name
touch $f3name

ls
