read -p"please enter the student name: " stud_name
read -p"please enter the student marks: " stud_marks

echo "----Student Details----"
echo "Name = $stud_name"
echo "Marks = $stud_marks"
if [ $stud_marks -ge 90 ] && [ $stud_marks -le 100 ]
then
 echo "Grade: A"
elif [ $stud_marks -ge 75 ] && [ $stud_marks -le 89 ]
then 
 echo "Grade: B"
elif [ $stud_marks -ge 60 ] && [ $stud_marks -le 70 ]
then 
 echo "Grade: C"
elif [ $stud_marks -ge 50 ] && [ $stud_marks -le 59 ]
then 
 echo "Grade: D"
elif [ $stud_marks -lt 50] && [ $stud_marks -ge 0 ]
then 
 echo "Fail"
else
  echo "Invalid grade, enter the valid garde"
fi
