read -p " please enter a number from 0 to 100: " num
sum=0
reverse_num=""


while [ $num -gt 0 ]
do
  temp=$((num % 10))
  reverse_num="$reverse_num$temp"
  sum=$((sum + temp))
  num=$((num/10))
  
done
echo "Sum = $sum"
echo "Reverse = $reverse_num"
