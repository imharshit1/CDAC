read -p"Enter the name of the source file: " sfile
read -p"Enter the name of the destination file: " dfile

if [ -f "$sfile" ]
then
cp "$sfile" "$dfile"
echo "Copied successfully"

else
echo "The source file doesn't exsit"
fi
