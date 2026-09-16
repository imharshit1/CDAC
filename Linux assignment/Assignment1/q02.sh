echo "Enter the principal Amount:"
read amount
echo "Enter the simple interest:"
read interest
echo "Enter the numbers of years :"
read duration
simpleinterest=$(((amount*interest*duration)/100))
totalamount=$((amount+simpleinterest))
echo "principal Amount:$amount"
echo "simple interest $simpleinterest"
echo "total Amount:$totalamount"


