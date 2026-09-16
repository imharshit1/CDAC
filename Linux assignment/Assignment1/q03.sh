read -p"Enter the number of electricity units consumed: " units
echo $units

bill=0
if [ $units -le 100 ]
then
bill=$((2 * units))

elif [ $units -le 200 ]
then
bill=$((2 * 100 + (units-100) * 3))

elif [ $units -le 300 ]
then
bill=$((2 * 100 + 3 *100 + 5 * (units-200)))

else
bill=$((2 *100 + 3 *100 + 5 * 100 + 7 *(units - 300)))

fi
echo "Bill = $bill"

