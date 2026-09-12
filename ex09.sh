read -p"enter the file name: " fname

if [ -f "$fname" ]
then
ls
size=$(wc -c < "$fname")
lines=$(wc -l < "$fname")
words=$(wc -w < "$fname")
char=$(wc -m < "$fname")


echo "Size of the file: $size"
echo "Number of lines: $lines"
echo "Number of words: $words"
echo "Number of character: $char"

else
echo "File not found"

fi

