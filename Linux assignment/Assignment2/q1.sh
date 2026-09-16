read -p"Enter the name of the file: " dname
if [ -f "$dname" ]
then 
bytes=$(wc -c < "$dname")
lines=$(wc -l < "$dname")
words=$(wc -w < "$dname")
char=$(wc -m < "$dname")

echo "size: $bytes
lines: $lines
words: $words
characters: $char"

else
echo "$dname doesn't exist"
fi
